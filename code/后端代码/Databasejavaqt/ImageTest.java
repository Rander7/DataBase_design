//*******************************数据库课设 第21组******************************************
//******************************任晨玮 张飒儒 李明翰*****************************************
//***********************该java类功能:将从数据库中取出图片二进制并转换png输出**********************

package Databasejavaqt;

//从数据库中取出图片二进制并转换png输出
import java.io.ByteArrayInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;

public class ImageTest {
    public static void main(String[] args){
        db_to_png(7);
    }
    public static void db_to_png(int cid) {
        String connectionString = "jdbc:sqlserver://localhost:1433;databaseName=csharpdatabase;user=sa;password=123456";
        String tableName = "t_class";
        String columnName = "图片";
        String outputFilePath = "C:\\Users\\rcw25\\Desktop\\picture\\final_class\\output.png";
        String ssql="SELECT " + columnName + " FROM " + tableName+" where 类别ID = "+cid;

        try {
            // 从SQL Server中获取image类型数据
            byte[] imageData = retrieveImageDataFromSQLServer(connectionString, tableName, columnName,ssql);

            // 将字节数组转换为16进制字符串
            String hexData = byteArrayToHex(imageData);

            // 从16进制字符串中恢复BMP图像
            BufferedImage image = restoreBMPImageFromHex(hexData);

            // 将BMP图像转换为PNG并保存到计算机上
            savePNGImage(image, outputFilePath);

            System.out.println("图像已保存到：" + outputFilePath);
        } catch (SQLException | IOException e) {
            e.printStackTrace();
        }
    }

    // 从SQL Server中获取image类型数据
    private static byte[] retrieveImageDataFromSQLServer(String connectionString, String tableName, String columnName,String ssql) throws SQLException {
        try (Connection connection = DriverManager.getConnection(connectionString);

             PreparedStatement statement = connection.prepareStatement(ssql);
             ResultSet resultSet = statement.executeQuery()) {
            if (resultSet.next()) {
                return resultSet.getBytes(1);
            }
        }
        return null;
    }

    // 将字节数组转换为16进制字符串
    private static String byteArrayToHex(byte[] byteArray) {
        StringBuilder hexData = new StringBuilder();
        for (byte b : byteArray) {
            String hex = String.format("%02X", b);
            hexData.append(hex);
        }
        return hexData.toString();
    }

    // 从16进制字符串中恢复BMP图像
    private static BufferedImage restoreBMPImageFromHex(String hexData) throws IOException {
        byte[] imageData = hexToByteArray(hexData);
        ByteArrayInputStream inputStream = new ByteArrayInputStream(imageData);
        return ImageIO.read(inputStream);
    }

    // 将BMP图像转换为PNG并保存到计算机上
    private static void savePNGImage(BufferedImage image, String filePath) throws IOException {
        FileOutputStream outputStream = new FileOutputStream(filePath);
        ImageIO.write(image, "png", outputStream);
        outputStream.close();
    }

    // 将16进制字符串转换为字节数组
    private static byte[] hexToByteArray(String hexData) {
        int len = hexData.length() / 2;
        byte[] byteArray = new byte[len];
        for (int i = 0; i < len; i++) {
            String byteStr = hexData.substring(2 * i, 2 * (i + 1));
            byteArray[i] = (byte) Integer.parseInt(byteStr, 16);
        }
        return byteArray;
    }
}
