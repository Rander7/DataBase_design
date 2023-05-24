//*******************************数据库课设 第21组******************************************
//******************************任晨玮 张飒儒 李明翰*****************************************
//***********************该java类功能:原始16进制数据处理后存在数据库****************************
package Databasejavaqt;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class ImageTransform {
    public static void main(String[] args) {
        String filePath = "C:\\Users\\rcw25\\Desktop\\picture\\final_class\\444.txt";
        int charactersToRemove = 158;
        String connectionString = "jdbc:sqlserver://localhost:1433;databaseName=csharpdatabase;user=sa;password=123456";
        String tableName = "t_class";
        String columnName = "图片";
        //修改id
        int id=8;

        try {
            // 读取文本文件中的16进制数据
            String hexData = readHexDataFromFile(filePath);

            // 删除前面指定数量的16进制字符
            String trimmedHexData = trimHexData(hexData, charactersToRemove);

            // 保存修改后的16进制数据到原始文件中
            saveHexDataToFile(trimmedHexData, filePath);

            // 将修改后的16进制数据转换为字节数组
            byte[] byteArray = hexToByteArray(trimmedHexData);

            // 将字节数组保存到SQL Server的image类型字段中
            saveByteArrayToSQLServer(byteArray, connectionString, tableName, columnName,id);

            System.out.println("数据处理完成！");
        } catch (IOException | SQLException e) {
            e.printStackTrace();
        }
    }

    // 读取文本文件中的16进制数据
    private static String readHexDataFromFile(String filePath) throws IOException {
        StringBuilder hexData = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                hexData.append(line.trim());
            }
        }
        return hexData.toString();
    }

    // 删除前面指定数量的16进制字符
    private static String trimHexData(String hexData, int charactersToRemove) {
        return hexData.substring(charactersToRemove);
    }

    // 保存修改后的16进制数据到原始文件中
    private static void saveHexDataToFile(String hexData, String filePath) throws IOException {
        try (FileWriter writer = new FileWriter(filePath, StandardCharsets.UTF_8)) {
            writer.write(hexData);
        }
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

    // 将字节数组保存到SQL Server的image类型字段中
    private static void saveByteArrayToSQLServer(byte[] byteArray, String connectionString, String tableName, String columnName,int id) throws SQLException {
        try (Connection connection = DriverManager.getConnection(connectionString);
             PreparedStatement statement = connection.prepareStatement("UPDATE " + tableName + " SET " + columnName + " = ? where 类别ID = ?")) {
            statement.setBytes(1, byteArray);
            statement.setInt(2, id);
            statement.executeUpdate();
        }
    }
}



























