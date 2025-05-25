#include <iostream>

int main() {
    std::unordered_map<std::string, std::string> vocal_to_texte = {
        {"a", "Alfa"},  // Alfa is the first letter in the alphabet.
        {"e", "Echo"},
        {"i", "India"},
        {"o", "Oscar"},
        {"u", "Uniform"}
    };
    
    for (const auto &pair : vocal_to_texte) {
        if (vocal_to_texte.count(pair.first)) {
            std::cout << pair.second << ", ";
        } else {
            std::cerr << "Missing: " << pair.first;
        }
    }
    
    return 0;
} catch (const std::exception& e) {
    std::cerr << "Exception: " << e.what();
    return 1;
} catch (...) {
    std::cerr << "Unknown exception.anding: " << std::endl; // NOLINT
    return 2;
}
/* Output:
Alfa, Echo, India, Oscar, Uniform, Missing: i
*/