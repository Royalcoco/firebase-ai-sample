pragma solidity ^0.8.0;

contract NewGenerationToken {
    string public name = "NewGenerationToken";
    string public symbol = "NGT";
    uint8 public decimals = 18;
    uint256 public totalSupply = 31000000 * 10 ** uint256(decimals);
    address public owner;
    mapping (address => uint256) public balanceOf;
    mapping (address => mapping (address => uint256)) public allowance;
    mapping (address => bool) public frozenAccount;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event FrozenFunds(address target, bool frozen);
    event SupplyChanged(uint256 newSupply);

    constructor() {
        owner = msg.sender;
        balanceOf[msg.sender] = totalSupply;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(!frozenAccount[msg.sender], "Account is frozen");
        require(balanceOf[msg.sender] >= _value);
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(!frozenAccount[_from], "Account is frozen");
        require(_value <= balanceOf[_from]);
        require(_value <= allowance[_from][msg.sender]);
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }

    function freezeAccount(address target, bool freeze) public onlyOwner {
        frozenAccount[target] = freeze;
        emit FrozenFunds(target, freeze);
    }

    function mintToken(uint256 amount) public onlyOwner {
        totalSupply += amount;
        balanceOf[owner] += amount;
        emit SupplyChanged(totalSupply);
    }

    function burnToken(uint256 amount) public onlyOwner {
        require(balanceOf[owner] >= amount, "Insufficient balance");
        totalSupply -= amount;
        balanceOf[owner] -= amount;
        emit SupplyChanged(totalSupply);
    }
}
