import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Consumer;

import javax.imageio.ImageIO;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.EncodeHintType;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.WriterException;
import com.google.zxing.client.j2se.MatrixToImageWriter;
import com.google.zxing.common.BitMatrix;
import org.web3j.protocol.Web3j;
import org.web3j.protocol.core.methods.response.TransactionReceipt;
import org.web3j.protocol.http.HttpService;
import org.web3j.tx.TransactionManager;
import org.web3j.tx.gas.StaticGasProvider;

public class DecentralizedLibrary {
    private Map<String, Consumer<String>> codeLibrary;

    public DecentralizedLibrary() {
        codeLibrary = new HashMap<>();
    }

    public void addCode(String key, Consumer<String> codeFunction) {
        codeLibrary.put(key, codeFunction);
    }

    public void executeCode(String key, String parameter) {
        if (codeLibrary.containsKey(key)) {
            codeLibrary.get(key).accept(parameter);
        } else {
            System.out.println("Code not found for key: " + key);
        }
    }

    public static void main(String[] args) {
        DecentralizedLibrary library = new DecentralizedLibrary();

        library.addCode("A", (String outputPath) -> {
            try {
                // Generate Banana Image
                int width = 600, height = 600;
                BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);
                Graphics2D g = image.createGraphics();

                // Set background color
                g.setColor(Color.WHITE);
                g.fillRect(0, 0, width, height);

                // Draw banana shape
                g.setColor(Color.YELLOW);
                g.fillOval(200, 200, 200, 100);

                // Add text
                g.setColor(Color.BLACK);
                g.setFont(new Font("Arial", Font.BOLD, 20));
                g.drawString("Banana NFT", 250, 300);

                g.dispose();

                // Save image
                ImageIO.write(image, "png", new File(outputPath));
                System.out.println("Banana NFT saved to " + outputPath);
            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        library.addCode("B", (String data) -> {
            try {
                // Create QR Code
                String filePath = "qr_code.png";
                int width = 300, height = 300;
                Map<EncodeHintType, Object> hints = new HashMap<>();
                hints.put(EncodeHintType.ERROR_CORRECTION, com.google.zxing.qrcode.decoder.ErrorCorrectionLevel.L);
                BitMatrix bitMatrix = new MultiFormatWriter().encode(data, BarcodeFormat.QR_CODE, width, height, hints);
                MatrixToImageWriter.writeToPath(bitMatrix, "PNG", Paths.get(filePath));
                System.out.println("QR code saved to " + filePath);
            } catch (WriterException | IOException e) {
                e.printStackTrace();
            }
        });

        library.addCode("C", (String outputPath) -> {
            // Placeholder for IPFS upload function
            System.out.println("Upload to IPFS: " + outputPath);
        });

        library.addCode("D", (String argsStr) -> {
            String[] args = argsStr.split(",");
            if (args.length < 4) {
                System.out.println("Invalid arguments for minting NFT");
                return;
            }
            String videoPath = args[0];
            String contractAddress = args[1];
            String privateKey = args[2];
            String accountAddress = args[3];

            // Placeholder for minting NFT on Ethereum
            System.out.println("Mint NFT with video path: " + videoPath);
            System.out.println("Contract Address: " + contractAddress);
            System.out.println("Private Key: " + privateKey);
            System.out.println("Account Address: " + accountAddress);
        });

        // Test the code
        library.executeCode("A", "banana_nft.png"); // Create and save banana image
        library.executeCode("B", "https://your.ipfs.gateway/galaxy_rotation.mp4"); // Create and save QR code
        library.executeCode("C", "galaxy_rotation.mp4"); // Placeholder for IPFS upload
        library.executeCode("D", "galaxy_rotation.mp4,0xYourContractAddress,0xYourPrivateKey,0xYourAccountAddress"); // Placeholder for minting NFT
    }
}

// Output:
// Banana NFT saved to banana_nft.png
// QR code saved to qr_code.png
// Upload to IPFS: galaxy_rotation.mp4
// Mint NFT with video path: galaxy_rotation.mp4
// Contract Address: 0xYourContractAddress
// Private Key: 0xYourPrivateKey
// Account Address: 0xYourAccountAddress
```

In this example, we have created a `DecentralizedLibrary` class that allows us to add different code snippets with a key and execute them based on the key. We have added four code snippets for creating and saving a banana image, generating a QR code, uploading to IPFS, and minting an NFT on Ethereum. The `executeCode` method takes a key and a parameter, and it executes the code snippet associated with that key.
