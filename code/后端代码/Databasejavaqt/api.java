//*******************************数据库课设 第21组******************************************
//******************************任晨玮 张飒儒 李明翰*****************************************
//***************该java类功能:将所有数据库操作方法集成到一个api类中,方便前端PYQT调用*****************
//**************************每个方法都有注释简述该方法作用**************************************
//******************在IDEA中打开可以使用快捷键 Ctrl+F12 快速查看该类所有方法名*********************

package Databasejavaqt;

import java.io.*;
import java.sql.*;
import java.io.BufferedOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Random;
import java.io.ByteArrayInputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;


public class api {
    public static final int ll=20000;
    public static int user_xiadan_id=0;
    public static String g_user_idd=null;
    public static int g_worker_idd=0;
    public static String g_newordertime=null;


    //随机生成5位大写字母id
    public static String generateRandomString(int length) {
        StringBuilder sb = new StringBuilder(length);
        Random random = new Random();
        for (int i = 0; i < length; i++) {
            char randomChar = (char) (random.nextInt(26) + 'A');
            sb.append(randomChar);
        }
        return sb.toString();
    }

    public static String[] g_user_id = new String[ll];
    public static String[] g_user_ename = new String[ll];
    public static String[] g_user_name = new String[ll];
    public static String[] g_user_zw = new String[ll];
    public static String[] g_user_ads = new String[ll];
    public static String[] g_user_city = new String[ll];
    public static String[] g_user_area = new String[ll];
    public static String[] g_user_cod = new String[ll];
    public static String[] g_user_nation = new String[ll];
    public static String[] g_user_tel = new String[ll];
    public static String[] g_user_cz = new String[ll];
    public static String[] g_user_psw = new String[ll];
    public static int g_user_len=0;
    //用户注册
    public static String add_user(String ename,String name,String wor,String ads,String city,String area,String cod,String nation,String tel,String cz,String pw)
    {
        Connection conn=null;
        PreparedStatement pstmt=null;
        String kid=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn= DriverManager.getConnection(url,user,password);

            while(true){
                kid = generateRandomString(5);
                if(!user_id_exists(kid)){
                    break;
                }
            }

            ResultSet res=null;

            String sql="insert into t_user"+
                    "(客户ID,公司名称,联系人姓名,联系人职务,地址,城市,地区,邮政编码,国家,电话,传真,psw)"+
                    "values(?,?,?,?,?,?,?,?,?,?,?,?)";
            pstmt=conn.prepareStatement(sql);

            pstmt.setString(1, kid);
            pstmt.setString(2, ename);
            pstmt.setString(3, name);
            pstmt.setString(4,wor);
            pstmt.setString(5,ads);
            pstmt.setString(6, city);
            pstmt.setString(7,area);
            pstmt.setString(8,cod);
            pstmt.setString(9,nation);
            pstmt.setString(10,tel);
            pstmt.setString(11,cz);
            pstmt.setString(12,pw);


            int result=pstmt.executeUpdate();
            System.out.println(String.format("数据库保存了%d个客户", result));
            return kid;
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null){
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
        return kid;
    }

    public static int[] g_worker_id=new int[ll];
    public static String[] g_worker_xs=new String[ll];
    public static String[] g_worker_name=new String[ll];
    public static String[] g_worker_zw=new String[ll];
    public static String[] g_worker_zc=new String[ll];
    public static String[] g_worker_time1=new String[ll];
    public static String[] g_worker_time2=new String[ll];
    public static String[] g_worker_ads=new String[ll];
    public static String[] g_worker_city=new String[ll];
    public static String[] g_worker_area=new String[ll];
    public static String[] g_worker_cod=new String[ll];
    public static String[] g_worker_nation=new String[ll];
    public static String[] g_worker_tel=new String[ll];
    public static String[] g_worker_fj=new String[ll];
    public static String[] g_worker_zp=new String[ll];
    public static String[] g_worker_bz=new String[ll];
    public static int[] g_worker_sj=new int[ll];
    public static String[] g_worker_psw=new String[ll];
    public static int g_worker_len=0;



    //雇员注册
    //这个照片也是把图片地址传进来，不过这个规定了数据库里面存放的是图片地址，类别里面存放的是图片二进制代码，但是前端传递的是相同的，都是地址
    //这个上级，设置了是int，对于空(null)情况传递0进来，int不能赋值null，加了判断，如果是0就赋值进null！
    public static void add_worker(String ename,String name,String wor,String zc,String datetime1,String datetime2,String ads,String city,String area,String cod,String nation,String tel,String fj,String zp,String bz,int sj,String pw)
    {
        Connection conn=null;
        PreparedStatement pstmt=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);


            ResultSet res=null;

            String str="select max(雇员ID) cd from t_worker";
            pstmt=conn.prepareStatement(str);
            res = pstmt.executeQuery();
            int nid=0;
            while(res.next()){
                nid=res.getInt("cd");
                nid+=1;
            }

            String sql="insert into t_worker"+
                    "(雇员ID,姓氏,名字,职务,尊称,出生日期,雇用日期,地址,城市,地区,邮政编码,国家,家庭电话,分机,照片,备注,上级,psw)"+
                    "values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)";
            pstmt=conn.prepareStatement(sql);
//
            pstmt.setInt(1, nid);
            pstmt.setString(2, ename);
            pstmt.setString(3, name);
            pstmt.setString(4,wor);
            pstmt.setString(5, zc);
            pstmt.setString(6, datetime1);
            pstmt.setString(7,datetime2);
            pstmt.setString(8, ads);
            pstmt.setString(9, city);
            pstmt.setString(10,area);
            pstmt.setString(11,cod);
            pstmt.setString(12,nation);
            pstmt.setString(13,tel);
            pstmt.setString(14,fj);
            pstmt.setString(15,zp);
            pstmt.setString(16,bz);
            if(sj==0){
                pstmt.setString(17,null);
            }
            else{
                pstmt.setInt(17,sj);
            }
            pstmt.setString(18,pw);


            int result=pstmt.executeUpdate();
            System.out.println(String.format("数据库保存了%d个雇员", result));
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null){
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }
    public static int[] g_class_id=new int[ll];
    public static String[] g_class_name=new String[ll];
    public static String[] g_class_sm=new String[ll];
    //图片存在电脑上，根据数目直接找
    public static int g_class_len=0;



    //主页：展示所有类别
    //这里没有传参，到时候可能要改一下，随便传一个假参数，直接String[] args好像有问题
    public static void show_all_class() {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select* from t_class where 类别ID is not NULL  ";

            ResultSet res=null;
            res = stat1.executeQuery(str);

            g_class_len=0;
            int ii=0;

            //读取到的类别图片保存的地址


            while(res.next()){
                String outputFilePath = "C:\\Users\\rcw25\\Desktop\\picture\\final_class\\output\\"+ii+".png";
                g_class_id[ii]=res.getInt(1);
                g_class_name[ii]=res.getString(2);
                g_class_sm[ii]=res.getString(3);

                db_to_png(outputFilePath,g_class_id[ii]);

                System.out.println(g_class_id[ii]+","+g_class_name[ii]+","+g_class_sm[ii]);

                ii++;
            }
            g_class_len=ii;

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }
    public static int[] g_product_id=new int[ll];
    public static String[] g_product_name=new String[ll];
    public static String[] g_product_num=new String[ll];
    public static String[] g_product_money=new String[ll];
    public static Short[] g_product_kcl=new Short[ll];
    public static Short[] g_product_dgl=new Short[ll];
    public static Short[] g_product_zdgl=new Short[ll];
    public static boolean[] g_product_zz=new boolean[ll];

    public static int g_product_len=0;

    //传递类别id，展示该类别所有商品
    public static void show_all_class_product() {
        String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
        String username = "sa";
        String password = "123456";


        //展示所有商品的名称,单价，库存量，对应类别图片(未来有对应物品图片)
        //有自己图片就用自己图片，没有就用类别图片，如果都没有，展示默认图片
        //这里把自己的图片和对应图片取出，先暂时用类别的图片

        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            Connection connection = DriverManager.getConnection(url, username, password);

            String sql = "SELECT t_product.产品ID,t_product.产品名称, t_product.单位数量, t_product.单价, t_product.库存量,t_product.图片,t_class.类别名称,t_class.图片 " +
                    "FROM t_product,t_class,t_shuyu WHERE t_product.产品ID=t_shuyu.产品ID and t_shuyu.类别ID=t_class.类别ID and t_product.中止=0";
            PreparedStatement statement = connection.prepareStatement(sql);

            ResultSet resultSet = statement.executeQuery();

            int ii=0;
            g_product_len=0;

            while(resultSet.next()){
                String outputFilePath = "C:\\Users\\rcw25\\Desktop\\picture\\final_class\\"+ii+".jpg";
                g_product_id[ii]=resultSet.getInt(1);
                g_product_name[ii]=resultSet.getString(2);
                g_product_num[ii]=resultSet.getString(3);
                g_product_money[ii]=resultSet.getString(4);
                g_product_kcl[ii]=resultSet.getShort(5);
                ii++;

            }
            g_product_len=ii;

            resultSet.close();


            statement.close();
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }


    //选择一个商品，展示该商品所有属性
    public static void show_one_product(int id1) {
        String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
        String username = "sa";
        String password = "123456";

        //展示该商品的名称，数量，单价，库存量，对应类别图片(未来有对应物品图片),供应商信息
        //有自己图片就用自己图片，没有就用类别图片，如果都没有，展示默认图片

        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            Connection connection = DriverManager.getConnection(url, username, password);

            String sql = "SELECT t_product.*,t_class.类别名称,t_class.图片 " +
                    "FROM t_product,t_class,t_shuyu WHERE t_product.产品ID=t_shuyu.产品ID and t_shuyu.类别ID=t_class.类别ID and t_product.产品ID= ?";
            PreparedStatement statement = connection.prepareStatement(sql);

            statement.setInt(1,id1);

            ResultSet resultSet = statement.executeQuery();
            while(resultSet.next()){
                //太多了，想要哪个要哪个，产品所有信息都在里面,就是产品的供应商没有
                String name=resultSet.getString(1);
                String dwnum=resultSet.getString(2);
                String price=resultSet.getString(3);
                short kc=resultSet.getShort(4);
                String pimage=resultSet.getString(5);
                String cname=resultSet.getString(6);
                String cimage=resultSet.getString(7);



//                image_to_hex(cimage,id1);
                System.out.println(name+","+dwnum+","+price+","+kc+","+pimage+","+cname+","+cimage);
            }

            Statement stat=null;
            stat = connection.createStatement();


            //供应商国家，城市，公司名称
            String sql1 = "SELECT t_provider.国家,t_provider.城市,t_provider.公司名称 " +
                    "FROM t_product,t_provider,t_gongying WHERE t_product.产品ID=t_gongying.产品ID and t_gongying.供应商ID=t_provider.供应商ID and t_product.产品ID= "+id1;

            ResultSet resultSet1 = stat.executeQuery(sql1);
            while(resultSet1.next()){
                //太多了，想要哪个要哪个，产品所有信息都在里面,就是产品的供应商没有
                String nation=resultSet1.getString(1);
                String city=resultSet1.getString(2);
                String name=resultSet1.getString(3);

                System.out.println(nation+","+city+","+name);
            }

            statement.close();
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }


//    获取当前时间字符串
    public static String time_get() {
        // 获取当前时间
        LocalDateTime currentTime = LocalDateTime.now();

        // 定义日期时间格式
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");

        // 格式化当前时间为字符串
        String formattedTime = currentTime.format(formatter);


        // 保存在字符串变量中
        String timeString = formattedTime;
        return timeString;
    }
    public static int[] g_xiashu_id=new int[ll];
    public static int g_xiashu_len=0;
    public static int[] g_xiadan_id=new int[ll];
    public static String[] g_xiadan_uid=new String[ll];
    public static int[] g_xiadan_gid=new int[ll];
    public static String[] g_xiadan_tel=new String[ll];
    public static String[] g_xiadan_xtime=new String[ll];
    public static String[] g_xiadan_ttime=new String[ll];
    public static String[] g_xiadan_name=new String[ll];
    public static String[] g_xiadan_city=new String[ll];
    public static String[] g_xiadan_cod=new String[ll];
    public static String[] g_xiadan_nation=new String[ll];
    public static String[] g_xiadan_ads=new String[ll];
    public static String[] g_xiadan_area=new String[ll];
    public static int g_xiadan_len=0;


    //开局登录注册调用一次，给用户id给后端
    public static void u_xiadan(String nid)
    {
        //id给全局
        g_user_idd=nid;
        //找出用户所有信息
        select_user(nid);
        //获取当前时间字符串
        g_newordertime=time_get();
        //创建一个购物车
        add_xiadan_user(nid,g_user_tel[0],g_newordertime,g_user_name[0],g_user_city[0],g_user_cod[0],g_user_nation[0],g_user_ads[0],g_user_area[0]);
    }

    //点击最终的提交购物车调用，根据当前全局的用户id创建一个购物车
    public static int neworder()
    {
        g_newordertime=time_get();
        int id = user_xiadan_id;
        add_xiadan_user(g_user_idd,g_user_tel[0],g_newordertime,g_user_name[0],g_user_city[0],g_user_cod[0],g_user_nation[0],g_user_ads[0],g_user_area[0]);
        return id;
    }

    //建立购物车
    public static void add_xiadan_user(String id1,String tel,String time1,String kname,String city,String cod,String nation,String ads,String area) {
        Connection conn=null;
        PreparedStatement pstmt=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            ResultSet res=null;


            //给下单表赋下单id，在订单表中找最大的然后+1
            String str="select max(下单ID) cd from t_xiadan";
            pstmt=conn.prepareStatement(str);
            res = pstmt.executeQuery();

            user_xiadan_id=1;
            while(res.next()){
                user_xiadan_id=res.getInt("cd");
                user_xiadan_id+=1;
            }

            String sql="insert into t_xiadan"+
                    "(下单ID,客户ID,客户电话,下单时间,货主名称,货主城市,货主邮政编码,货主国家,货主地址,货主地区)"+
                    "values(?,?,?,?,?,?,?,?,?,?)";
            pstmt=conn.prepareStatement(sql);

            pstmt.setInt(1,user_xiadan_id);
            pstmt.setString(2, id1);
            pstmt.setString(3, tel);
            pstmt.setString(4,time1);
            pstmt.setString(5, kname);
            pstmt.setString(6, city);
            pstmt.setString(7,cod);
            pstmt.setString(8, nation);
            pstmt.setString(9,ads);
            pstmt.setString(10, area);

            int result=pstmt.executeUpdate();

            //返回下单id，通过这个下单id继续购买
            System.out.println(user_xiadan_id);


        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //给购物车中添加商品及其数量，多次使用，每添加一个调用一次
    public static void add_product_user(int cid,int num) {
        Connection conn=null;
        PreparedStatement pstmt=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            ResultSet res=null;

            //同时把返回的商品id和数量信息结合下单id插入下单明细表

            Statement stat=null;
            stat = conn.createStatement();
            int i=0;

            //供应商国家，城市，公司名称
            String sql1 = "insert into t_xiadandetail"+
                    "(下单ID,产品ID,数量)"+
                    "values("+user_xiadan_id+","+cid+","+num+")";

            stat.executeUpdate(sql1);


        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //点击提交之后这边其实没有改变，因为下单表已经存在于数据库中，暂时还不支持删除购物车中东西，点击提交后那个bool类型恢复，再加入购物车先创建一个新的购物车


    //雇员在对下单表操作之前点击时候先判断是否是同一人，如果是则不能进行操作
    //传进来是雇员准备操作的订单的id,这里不能判断，要读取到前端，因为这里没有雇员电话信息！！！！
    public static void worker_xiadan_judge(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            String stt="select 客户电话 from t_xiadan where 下单ID = "+did;
            Statement statttt=conn.createStatement();
            ResultSet resss=null;
            resss = statttt.executeQuery(stt);

            while(resss.next()){
                //这个就是订单中的客户电话，把这个取到python和雇员电话判断
                //如果一样，就提示不能操作，啥也不调用，如果不一样，根据通过与否分别调用下面两个函数
                String dh= resss.getString(1);
                System.out.println(dh);
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //登录职工时候调用一次，获取职工所有信息在全局
    public static void u_worker(int nid)
    {
        g_worker_idd=nid;
    }

    //雇员通过下单内容
    public static void add_xiadan_worker_tg(int xiadanid) {
        Connection conn=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            //其实雇员这里不是增加，而是更新下单表，并且把下单表的数据联合下单明细一起添加到订单表和订单明细
            //而且如果不通过，还要把下单表和下单明细中的该下单id对应数据删除
            //所以整体流程是，客户再xiadan和xiandandetail增加信息后，worker增加一个确定日期然后确定通过
            //最后插入订单和订单明细表
            //前端需要传入：雇员通过时候的时间，用户是否通过该下单请求

            //这里换成前端传递进来的是否通过信息，前端要判断是否是同一个人(我觉得用电话)，下单表里有客户电话
            //通过就插入

            String sql1="update t_xiadan set 雇员ID=?,通过时间=? where 下单ID=?";
            PreparedStatement pstmt1=null;
            pstmt1=conn.prepareStatement(sql1);
            //这里改成前端返回的雇员ID,通过时间(格式2022-12-22 12:30)

            String ttt=time_get();

            pstmt1.setInt(1,g_worker_idd);
            pstmt1.setString(2, ttt);
            pstmt1.setInt(3, xiadanid);

            int result1=pstmt1.executeUpdate();
            System.out.println(String.format("数据库保存了%d个下单信息", result1));


            //用下单ID作为订单id插入order和odetail表


            Statement stat1=conn.createStatement();

            String str1="select * from t_xiadan where 下单ID = "+xiadanid;

            ResultSet res1=null;
            res1 = stat1.executeQuery(str1);

            while(res1.next()){

                //1234表示表列数，类型和数据库表属性类型相一致，优势：方便计算，如工资涨100可直接输出salary+100
                int id = res1.getInt(1);
                String kid=res1.getString(2);
                String gid=res1.getString(3);
                String tel=res1.getString(4);
                String xtime=res1.getString(5);
                String ttime=res1.getString(6);
                String kname=res1.getString(7);
                String city=res1.getString(8);
                String cod=res1.getString(9);
                String nation=res1.getString(10);
                String ads=res1.getString(11);
                String area=res1.getString(12);

                String sql2="insert into t_order"+
                        "(订单ID,订购日期,发货日期,到货日期,货款确认日期,运货费,货主名称,货主地址,货主城市,货主地区,货主邮政编码,货主国家,折扣ID,客户ID)"+
                        "values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)";
                PreparedStatement pstmt2=null;
                pstmt2=conn.prepareStatement(sql2);

                pstmt2.setInt(1,id);
                pstmt2.setString(2, xtime);
                //这里到时候发货日期到货日期要改，这里直接全用一个
                pstmt2.setString(3,xtime);
                pstmt2.setString(4,ttime);
                pstmt2.setString(5,ttime);
                pstmt2.setString(6,"10");
                pstmt2.setString(7,kname);
                pstmt2.setString(8,ads);
                pstmt2.setString(9,city);
                pstmt2.setString(10,area);
                pstmt2.setString(11,cod);
                pstmt2.setString(12,nation);
                pstmt2.setString(13,"11111");
                pstmt2.setString(14,kid);


                int result2=pstmt2.executeUpdate();
                System.out.println(String.format("数据库保存了%d个订单信息", result2));
            }
            res1.close();

            //同时把返回的商品id和数量信息结合下单id插入下单明细表

            String str2="select * from t_xiadandetail where 下单ID = "+xiadanid;

            ResultSet res2=null;
            Statement stat2=conn.createStatement();
            res2 = stat2.executeQuery(str2);

            while(res2.next()){

                //1234表示表列数，类型和数据库表属性类型相一致，优势：方便计算，如工资涨100可直接输出salary+100
                int id = res2.getInt(1);
                int cid=res2.getInt(2);
                Short num=res2.getShort(3);


                String sql3="insert into t_odetails"+
                        "(订单ID,产品ID,数量)"+
                        "values(?,?,?)";
                PreparedStatement pstmt3=null;
                pstmt3=conn.prepareStatement(sql3);

                pstmt3.setInt(1,id);
                pstmt3.setInt(2,cid);
                pstmt3.setShort(3,num);

                int result3=pstmt3.executeUpdate();
                System.out.println(String.format("数据库保存了%d个订单明细信息", result3));
            }
            res2.close();


        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //雇员不通过下单内容
    //不通过，直接给xiadan表的这个记录删除了！
    public static void add_xiadan_worker_btg(int did) {
        Connection conn=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            Statement stat3=null;
            stat3=conn.createStatement();

            String str="delete from t_xiadan where 下单ID = "+did;

            int count = stat3.executeUpdate(str);
            if(count>=1){
                System.out.println("xiadan删除成功");
            }
            else{
                System.out.println("xiadan删除失败");
            }

            //删除xiadandetail中对应所有信息,设置了级联，所以只需要删除xiadan

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }
    public static int[] g_order_id=new int[ll];
    public static String[] g_order_time1=new String[ll];
    public static String[] g_order_time2=new String[ll];
    public static String[] g_order_time3=new String[ll];
    public static String[] g_order_time4=new String[ll];
    public static String[] g_order_money=new String[ll];
    public static String[] g_order_name=new String[ll];
    public static String[] g_order_ads=new String[ll];
    public static String[] g_order_city=new String[ll];
    public static String[] g_order_area=new String[ll];
    public static String[] g_order_cod=new String[ll];
    public static String[] g_order_nation=new String[ll];
    public static String[] g_order_zkid=new String[ll];
    public static boolean[] g_order_qx=new boolean[ll];
    public static String[] g_order_kid=new String[ll];
    public static boolean[] g_order_rq1=new boolean[ll];
    public static boolean[] g_order_rq2=new boolean[ll];
    public static boolean[] g_order_rq3=new boolean[ll];

    public static int g_order_len=0;

    //展示所有历史订单
    public static void show_all_order() {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select* from t_order";

            ResultSet res=null;
            res = stat1.executeQuery(str);

            int ii=0;
            g_order_len=0;

            while(res.next()){

                g_order_id[ii]=res.getInt(1);
                g_order_time1[ii]=res.getString(2);
                g_order_time2[ii]=res.getString(3);
                g_order_time3[ii]=res.getString(4);
                g_order_time4[ii]=res.getString(5);
                g_order_money[ii]=res.getString(6);
                g_order_name[ii]=res.getString(7);
                g_order_ads[ii]=res.getString(8);
                g_order_city[ii]=res.getString(9);
                g_order_area[ii]=res.getString(10);
                g_order_cod[ii]= res.getString(11);
                g_order_nation[ii]=res.getString(12);
                g_order_zkid[ii]=res.getString(13);
                g_order_qx[ii]=res.getBoolean(14);
                g_order_kid[ii]=res.getString(15);
                g_order_rq1[ii]=res.getBoolean(16);
                g_order_rq2[ii]=res.getBoolean(17);
                g_order_rq3[ii]=res.getBoolean(18);

                ii++;

            }
            g_order_len=ii;

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //展示所有待通过订单(下单表)
    public static void show_all_xiadan() {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select* from t_xiadan";

            ResultSet res=null;
            res = stat1.executeQuery(str);

            int ii=0;
            g_xiadan_len=0;

            while(res.next()){

                g_xiadan_id[ii]=res.getInt(1);
                g_xiadan_uid[ii]=res.getString(2);
                g_xiadan_gid[ii]=res.getInt(3);
                g_xiadan_tel[ii]=res.getString(4);
                g_xiadan_xtime[ii]=res.getString(5);
                g_xiadan_ttime[ii]=res.getString(6);
                g_xiadan_name[ii]=res.getString(7);
                g_xiadan_city[ii]=res.getString(8);
                g_xiadan_cod[ii]= res.getString(9);
                g_xiadan_nation[ii]=res.getString(10);
                g_xiadan_ads[ii]=res.getString(11);
                g_xiadan_area[ii]=res.getString(12);

                ii++;

            }
            g_xiadan_len=ii;

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }


    //展示该用户下单的所有通过订单
    public static void show_order_tg() {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select* from t_order where 客户ID = "+"'"+g_user_idd+"'"+" and 取消=0 ";

            ResultSet res=null;
            res = stat1.executeQuery(str);

            int ii=0;
            g_order_len=0;

            while(res.next()){

                g_order_id[ii]=res.getInt(1);
                g_order_time1[ii]=res.getString(2);
                g_order_time2[ii]=res.getString(3);
                g_order_time3[ii]=res.getString(4);
                g_order_time4[ii]=res.getString(5);
                g_order_money[ii]=res.getString(6);
                g_order_name[ii]=res.getString(7);
                g_order_ads[ii]=res.getString(8);
                g_order_city[ii]=res.getString(9);
                g_order_area[ii]=res.getString(10);
                g_order_cod[ii]= res.getString(11);
                g_order_nation[ii]=res.getString(12);
                g_order_zkid[ii]=res.getString(13);
                g_order_qx[ii]=res.getBoolean(14);
                g_order_kid[ii]=res.getString(15);

                ii++;

            }
            g_order_len=ii;

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }


    //展示该用户下单的所有用户自己取消的订单(2.0)因为涉及用户再点击成功的订单进行更改，要级联退回商品修改库存之类的
    public static void show_order_qx() {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select* from t_order where 客户ID = "+"'"+g_user_idd+"'"+" and 取消=1 ";

            ResultSet res=null;
            res = stat1.executeQuery(str);

            int ii=0;
            g_order_len=0;

            while(res.next()){

                g_order_id[ii]=res.getInt(1);
                g_order_time1[ii]=res.getString(2);
                g_order_time2[ii]=res.getString(3);
                g_order_time3[ii]=res.getString(4);
                g_order_time4[ii]=res.getString(5);
                g_order_money[ii]=res.getString(6);
                g_order_name[ii]=res.getString(7);
                g_order_ads[ii]=res.getString(8);
                g_order_city[ii]=res.getString(9);
                g_order_area[ii]=res.getString(10);
                g_order_cod[ii]= res.getString(11);
                g_order_nation[ii]=res.getString(12);
                g_order_zkid[ii]=res.getString(13);
                g_order_qx[ii]=res.getBoolean(14);
                g_order_kid[ii]=res.getString(15);

                ii++;

            }
            g_order_len=ii;

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }
    public static int[] g_odetail_did=new int[ll];
    public static int[] g_odetail_pid=new int[ll];
    public static short[] g_odetail_num=new short[ll];
    public static int g_odetail_len=0;

    //通过订单id展示订单明细
    public static void select_odetails(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select* from t_odetails where 订单ID = "+did;

            ResultSet res=null;
            res = stat1.executeQuery(str);

            int ii=0;
            g_odetail_len=0;

            while(res.next()){

                g_odetail_did[ii]=res.getInt(1);
                g_odetail_pid[ii]=res.getInt(2);
                g_odetail_num[ii]=res.getShort(3);
                ii++;
            }
            g_odetail_len=ii;

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }


    //展示用户的购物车，其实就是把python存放的下单id传入，然后查下单明细表
    public static void select_xiadandetail(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select* from t_odetails where 下单ID = "+did;

            ResultSet res=null;
            res = stat1.executeQuery(str);

            int ii=0;
            g_odetail_len=0;

            while(res.next()){

                g_odetail_did[ii]=res.getInt(1);
                g_odetail_pid[ii]=res.getInt(2);
                g_odetail_num[ii]=res.getShort(3);

                ii++;
            }
            g_odetail_len=ii;

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }



    //判断供应商id是否存在
    public static boolean provider_exists(int did) {
        Connection conn = null;
        Statement stat1 = null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn = DriverManager.getConnection(url, user, password);

            stat1 = conn.createStatement();

            String str = "select 供应商ID from t_provider where 供应商ID = " + did;

            ResultSet res = null;
            res = stat1.executeQuery(str);

            while (res.next()) {
                int id = res.getInt(1);
                if(id==did){
                    return true;
                }
                else{
                    return false;
                }
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        } finally {
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if (stat1 != null) {
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
        return false;
    }

    //判断类别id是否存在
    public static boolean class_exists(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select 类别ID from t_class where 类别ID = "+did;

            ResultSet res=null;
            res = stat1.executeQuery(str);


            while(res.next()){
                int id1=res.getInt(1);
                if(id1==did){
                    return true;
                }
                else{
                    return false;
                }
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
        return false;
    }

    //判断用户id是否存在
    public static boolean user_id_exists(String kid) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select 客户ID from t_user where 客户ID = "+"'"+kid+"'";

            ResultSet res=null;
            res = stat1.executeQuery(str);


            while(res.next()){
                String id1=res.getString(1);
                if(id1.equals(kid)){
                    return true;
                }
                else{
                    return false;
                }
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
        return false;
    }



    //通过客户id读出用户信息
    public static void select_user(String did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select * from t_user where 客户ID = "+"'"+did+"'";

            ResultSet res=null;
            res = stat1.executeQuery(str);

            int ii=0;
            g_user_len=0;

            while(res.next()){

                //1234表示表列数，类型和数据库表属性类型相一致，优势：方便计算，如工资涨100可直接输出salary+100
                g_user_id[ii]= res.getString(1);
                g_user_ename[ii]=res.getString(2);
                g_user_name[ii]=res.getString(3);
                g_user_zw[ii]=res.getString(4);
                g_user_ads[ii]=res.getString(5);
                g_user_city[ii]=res.getString(6);
                g_user_area[ii]=res.getString(7);
                g_user_cod[ii]=res.getString(8);
                g_user_nation[ii]=res.getString(9);
                g_user_tel[ii]=res.getString(10);
                g_user_cz[ii]= res.getString(11);
                g_user_psw[ii]=res.getString(12);

            }
            g_user_len=ii;

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }


    //通过客户tel读出用户信息(下单时候需要,因为xiadan表要插入相关信息)
    public static void select_user_from_tel(String tel) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select * from t_user where 电话 = "+"'"+tel+"'";

            ResultSet res=null;
            res = stat1.executeQuery(str);

            int ii=0;
            g_user_len=0;

            while(res.next()){

                //1234表示表列数，类型和数据库表属性类型相一致，优势：方便计算，如工资涨100可直接输出salary+100
                g_user_id[ii]= res.getString(1);
                g_user_ename[ii]=res.getString(2);
                g_user_name[ii]=res.getString(3);
                g_user_zw[ii]=res.getString(4);
                g_user_ads[ii]=res.getString(5);
                g_user_city[ii]=res.getString(6);
                g_user_area[ii]=res.getString(7);
                g_user_cod[ii]=res.getString(8);
                g_user_nation[ii]=res.getString(9);
                g_user_tel[ii]=res.getString(10);
                g_user_cz[ii]= res.getString(11);
                g_user_psw[ii]=res.getString(12);

            }
            g_user_len=ii;

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }


    //通过雇员id读出用户信息(下单时候需要,因为xiadan表要插入相关信息)
    public static void select_worker(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select * from t_worker where 雇员ID = "+did;

            ResultSet res=null;
            res = stat1.executeQuery(str);

            g_worker_len=0;
            int ii=0;

            while(res.next()){

                //1234表示表列数，类型和数据库表属性类型相一致，优势：方便计算，如工资涨100可直接输出salary+100
                g_worker_id[ii]= res.getInt(1);
                g_worker_xs[ii]=res.getString(2);
                g_worker_name[ii]=res.getString(3);
                g_worker_zw[ii]=res.getString(4);
                g_worker_zc[ii]=res.getString(5);
                g_worker_time1[ii]=res.getString(6);
                g_worker_time2[ii]=res.getString(7);
                g_worker_ads[ii]=res.getString(8);
                g_worker_city[ii]=res.getString(9);
                g_worker_area[ii]=res.getString(10);
                g_worker_cod[ii]=res.getString(11);
                g_worker_nation[ii]=res.getString(12);
                g_worker_tel[ii]=res.getString(13);
                g_worker_fj[ii]=res.getString(14);
                g_worker_zp[ii]= res.getString(15);
                g_worker_bz[ii]=res.getString(16);
                g_worker_sj[ii]= res.getInt(17);
                g_worker_psw[ii]=res.getString(18);

               ii++;
            }
            g_worker_len=ii;


        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }


    //通过雇员tel读出信息
    public static void select_worker_from_tel(String tel) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select * from t_worker where 电话 = "+tel;

            ResultSet res=null;
            res = stat1.executeQuery(str);

            g_worker_len=0;
            int ii=0;

            while(res.next()){

                //1234表示表列数，类型和数据库表属性类型相一致，优势：方便计算，如工资涨100可直接输出salary+100
                g_worker_id[ii]= res.getInt(1);
                g_worker_xs[ii]=res.getString(2);
                g_worker_name[ii]=res.getString(3);
                g_worker_zw[ii]=res.getString(4);
                g_worker_zc[ii]=res.getString(5);
                g_worker_time1[ii]=res.getString(6);
                g_worker_time2[ii]=res.getString(7);
                g_worker_ads[ii]=res.getString(8);
                g_worker_city[ii]=res.getString(9);
                g_worker_area[ii]=res.getString(10);
                g_worker_cod[ii]=res.getString(11);
                g_worker_nation[ii]=res.getString(12);
                g_worker_tel[ii]=res.getString(13);
                g_worker_fj[ii]=res.getString(14);
                g_worker_zp[ii]= res.getString(15);
                g_worker_bz[ii]=res.getString(16);
                g_worker_sj[ii]= res.getInt(17);
                g_worker_psw[ii]=res.getString(18);

                ii++;
            }
            g_worker_len=ii;


        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //通过类别id读出所有类别信息
    public static void select_class(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select* from t_class where 类别ID = "+did;

            ResultSet res=null;
            res = stat1.executeQuery(str);

            g_class_len=0;
            int ii=0;

            //读取到的类别图片保存的地址


            while(res.next()){
                String outputFilePath = "C:\\Users\\rcw25\\Desktop\\picture\\final_class\\"+ii+".png";
                g_class_id[ii]=res.getInt(1);
                g_class_name[ii]=res.getString(2);
                g_class_sm[ii]=res.getString(3);

                db_to_png(outputFilePath,did);

                ii++;
            }
            g_class_len=ii;

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    public static int[] g_provider_id=new int[ll];
    public static String[] g_provider_ename=new String[ll];
    public static String[] g_provider_name=new String[ll];
    public static String[] g_provider_zw=new String[ll];
    public static String[] g_provider_ads=new String[ll];
    public static String[] g_provider_city=new String[ll];
    public static String[] g_provider_area=new String[ll];
    public static String[] g_provider_cod=new String[ll];
    public static String[] g_provider_nation=new String[ll];
    public static String[] g_provider_tel=new String[ll];
    public static String[] g_provider_cz=new String[ll];
    public static String[] g_provider_web=new String[ll];
    public static int g_provider_len=0;

    //通过供应商id读出供应商信息
    public static void select_provider(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select* from t_provider where 供应商ID = "+did;

            ResultSet res=null;
            res = stat1.executeQuery(str);

            int ii=0;
            g_provider_len=0;

            while(res.next()){

                //1234表示表列数，类型和数据库表属性类型相一致，优势：方便计算，如工资涨100可直接输出salary+100
                g_provider_id[ii]= res.getInt(1);
                g_provider_ename[ii]=res.getString(2);
                g_provider_name[ii]=res.getString(3);
                g_provider_zw[ii]=res.getString(4);
                g_provider_ads[ii]=res.getString(5);
                g_provider_city[ii]=res.getString(6);
                g_provider_area[ii]=res.getString(7);
                g_provider_cod[ii]=res.getString(8);
                g_provider_nation[ii]=res.getString(9);
                g_provider_tel[ii]=res.getString(10);
                g_provider_cz[ii]=res.getString(11);
                g_provider_web[ii]=res.getString(12);
                ii++;
            }
            g_provider_len=ii;

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }



    //新建商品时候添加供应
    public static void add_gongying(int pid,int cid) {
        Connection conn=null;
        PreparedStatement pstmt=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn = DriverManager.getConnection(url, user, password);

            ResultSet res = null;

            String sql="update t_gongying set 供应商ID=" +cid +"where 产品ID ="+pid;
            pstmt=conn.prepareStatement(sql);
            int result=pstmt.executeUpdate();
            System.out.println(String.format("数据库保存了%d个供应信息", result));
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null){
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }


    //新建商品时候添加类别
    public static void add_shuyu(int pid,int cid) {
        Connection conn=null;
        PreparedStatement pstmt=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn = DriverManager.getConnection(url, user, password);

            ResultSet res = null;

            String sql="update t_shuyu set 类别ID ="+cid+"where 产品ID="+pid;

            pstmt=conn.prepareStatement(sql);
            int result=pstmt.executeUpdate();
            System.out.println(String.format("数据库保存了%d个属于信息", result));
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null){
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }




    //增加新商品(雇员功能),同时增加供应商和类别，传递进来的时候要先调用provider_exists和class_exists判断输入的是否存在，到数据库这就直接插入了
    public static void add_product(String ename,String sl,String mon,Short rel,Short dgl,Short zdgl,Boolean zz,int gid,int cid) {
        Connection conn=null;
        PreparedStatement pstmt=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            ResultSet res=null;

            String str="select max(产品ID) cd from t_product";
            pstmt=conn.prepareStatement(str);
            res = pstmt.executeQuery();
            int nid=0;
            while(res.next()){
                nid=res.getInt("cd");
                nid+=1;
            }

            String sql="insert into t_product"+
                    "(产品ID,产品名称,单位数量,单价,库存量,订购量,再订购量,中止)"+
                    "values(?,?,?,?,?,?,?,?)";
            pstmt=conn.prepareStatement(sql);

            pstmt.setInt(1, nid);
            pstmt.setString(2, ename);
            pstmt.setString(3, sl);
            pstmt.setString(4,mon);
            pstmt.setShort(5, rel);
            pstmt.setShort(6, dgl);
            pstmt.setShort(7,zdgl);
            pstmt.setBoolean(8, zz);

            int result=pstmt.executeUpdate();
            System.out.println(String.format("数据库保存了%d个产品", result));

            add_gongying(nid,gid);
            add_shuyu(nid,cid);
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null){
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //添加新类别(雇员功能)
    public static void add_class(String cname,String shuoming,String tp) {
        Connection conn=null;
        PreparedStatement pstmt=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn= DriverManager.getConnection(url,user,password);

            ResultSet res=null;

            String str="select max(类别ID) cd from t_class";
            pstmt=conn.prepareStatement(str);
            res = pstmt.executeQuery();
            int nid=0;
            while(res.next()){
                nid=res.getInt("cd");
                nid+=1;
            }

            String sql="insert into t_class"+
                    "(类别ID,类别名称,说明)"+
                    "values(?,?,?)";
            pstmt=conn.prepareStatement(sql);

            pstmt.setInt(1, nid);
            pstmt.setString(2, cname);
            pstmt.setString(3, shuoming);
//          pstmt.setString(4,tp);
            int result=pstmt.executeUpdate();

//            image_to_hex(tp,nid);

            System.out.println(String.format("数据库保存了%d个类别", result));
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null){
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }


    //添加新供货商(雇员功能)
    //前端判断完全符合要求了再插进来，属于是最后一步，判断在python判断
    public static void add_provider(String ename,String name,String wor,String ads,String city,String area,String cod,String nation,String tel,String cz,String web)
    {
        Connection conn=null;
        PreparedStatement pstmt=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);


            ResultSet res=null;

            String str="select max(供应商ID) cd from t_provider";
            pstmt=conn.prepareStatement(str);
            res = pstmt.executeQuery();
            int nid=0;
            while(res.next()){
                nid=res.getInt("cd");
                nid+=1;
            }

            String sql="insert into t_provider"+
                    "(供应商ID,公司名称,联系人姓名,联系人职务,地址,城市,地区,邮政编码,国家,电话,传真,主页)"+
                    "values(?,?,?,?,?,?,?,?,?,?,?,?)";
            pstmt=conn.prepareStatement(sql);

            pstmt.setInt(1, nid);
            pstmt.setString(2, ename);
            pstmt.setString(3, name);
            pstmt.setString(4,wor);
            pstmt.setString(5, ads);
            pstmt.setString(6, city);
            pstmt.setString(7,area);
            pstmt.setString(8, cod);
            pstmt.setString(9, nation);
            pstmt.setString(10,tel);
            pstmt.setString(11,cz);
            pstmt.setString(12,web);

            int result=pstmt.executeUpdate();
            System.out.println(String.format("数据库保存了%d个供应商", result));
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null){
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }





    //通过电话判断用户是否存在
    public static boolean select_user_tel_exists(String tel) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select 电话 from t_user where 电话 ="+"'"+tel+"'";

            ResultSet res=null;
            res = stat1.executeQuery(str);



            while(res.next()){

                String tels=res.getString(1);
                if(tels.equals(tel)){
                    return true;
                }
                else{
                    return false;
                }
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
        return false;
    }


    //通过电话判断用户密码是否正确
    public static boolean select_user_psw_true(String tel,String psw) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select psw from t_user where 电话 = "+"'"+tel+"'";

            ResultSet res=null;
            res = stat1.executeQuery(str);

            while(res.next()){

                String psw1=res.getString(1);
                if(psw1.equals(psw)){
                    return true;
                }
                else{
                    return false;
                }
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
        return false;
    }


    //通过电话判断雇员用户是否存在
    public static boolean select_worker_tel_exists(String tel) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select 家庭电话 from t_worker where 家庭电话 = "+"'"+tel+"'";

            ResultSet res=null;
            res = stat1.executeQuery(str);

            while(res.next()){

                String tels=res.getString(1);
                if(tels.equals(tel)){
                    return true;
                }
                else{
                    return false;
                }
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
        return false;
    }





    //通过电话判断雇员密码是否正确
    public static boolean select_worker_psw_true(String tel,String psw) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select psw from t_worker where 电话 = "+"'"+tel+"'";

            ResultSet res=null;
            res = stat1.executeQuery(str);

            while(res.next()){

                String psw1=res.getString(1);
                if(psw1.equals(psw)){
                    return true;
                }
                else{
                    return false;
                }
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
        return false;
    }



    //通过id判断雇员id存不存在
    //通过电话判断雇员用户是否存在
    public static boolean select_worker_id_exists(int id) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select 雇员ID from t_worker where 雇员ID= "+id;

            ResultSet res=null;
            res = stat1.executeQuery(str);

            while(res.next()){


                int id1=res.getInt(1);

                if(id1==id){
                    return true;
                }
                else{
                    return false;
                }
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
        return false;
    }


    //通过id判断雇员密码是否正确
    public static boolean select_worker_psw_id_true(int id,String psw) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select psw from t_worker where 雇员ID = "+id;

            ResultSet res=null;
            res = stat1.executeQuery(str);

            while(res.next()){

                String psw1=res.getString(1);
                if(psw1.equals(psw)){
                    return true;
                }
                else{
                    return false;
                }
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
        return false;
    }


    //通过商品名查找商品
    public static void select_product(String pname) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select * from t_product where 产品名称 = "+pname;

            ResultSet res=null;
            res = stat1.executeQuery(str);

            while(res.next()){

                //1234表示表列数，类型和数据库表属性类型相一致，优势：方便计算，如工资涨100可直接输出salary+100
                int id = res.getInt(1);
                String name=res.getString(2);
                String num=res.getString(3);
                String mon=res.getString(4);
                Short kc=res.getShort(5);
                Short dg=res.getShort(6);
                Short zdg=res.getShort(7);
                boolean zz=res.getBoolean(8);

                System.out.println(id+","+name+","+name+","+num+","+mon+","+kc+","+dg+","+zdg+","+zz) ;
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }




    //查找商品供应信息
    public static void select_gongying(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select* from t_gongying where 产品ID = "+did;

            ResultSet res=null;
            res = stat1.executeQuery(str);

            while(res.next()){
                int id1=res.getInt(1);
                int id2=res.getInt(2);

                if(id2==0){
                    System.out.println(id1+",null");
                }
                else{
                    System.out.println(id1+","+id2);
                }

            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //查找商品类别信息
    public static void select_shuyu(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select* from t_shuyu where 产品ID = "+did;

            ResultSet res=null;
            res = stat1.executeQuery(str);

            while(res.next()){

                //1234表示表列数，类型和数据库表属性类型相一致，优势：方便计算，如工资涨100可直接输出salary+100
                int id1=res.getInt(1);
                int id2=res.getInt(2);

                if(id2==0){
                    System.out.println(id1+",null");
                }
                else{
                    System.out.println(id1+","+id2);
                }
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    public static int[] g_lingdao_gyid=new int[ll];
    public static int g_lingdao_len=0;

    public static int[] g_gongying_cid=new int[ll];
    public static int g_gongying_len=0;

    public static int[] g_shuyu_cid=new int[ll];
    public static int g_shuyu_len=0;


    //雇员查找领导id
    public static void select_lingdao(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select* from t_lingdao where 雇员ID = "+did;

            ResultSet res=null;
            res = stat1.executeQuery(str);

            while(res.next()){

                int id1=res.getInt(1);
                int id2=res.getInt(2);

                if(id2==0){
                    System.out.println(id1+",null");
                }
                else{
                    System.out.println(id1+","+id2);
                }

            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }


    //雇员查找下属信息,因为需要初始给其一个赋值，所以单独使用java时候赋值先
    public static void select_xiashu() {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            //因为需要初始给其一个赋值，所以单独使用java时候赋值先
            g_worker_idd=1;
            String str="select* from t_lingdao where 上级 = "+g_worker_idd;

            ResultSet res=null;
            res = stat1.executeQuery(str);
            int ii=0;
            g_xiashu_len=0;

            while(res.next()){

                g_xiashu_id[ii]=res.getInt(1);
                //从中找到名字
//                select_worker(g_xiashu_id[ii]);
                System.out.println(g_xiashu_id[ii]);
                ii++;

            }
            g_xiashu_len=ii;
            if(ii==0){
                System.out.println("没有下属");
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }



    //删除类别
    public static void delete_class(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="delete from t_class where 类别ID = "+did;

            int count = stat1.executeUpdate(str);
            if(count>=1){
                System.out.println("删除成功");
            }
            else{
                System.out.println("删除失败");
            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //删除供应商
    public static void delete_provider(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="delete from t_provider where 供应商ID = "+did;

            int count = stat1.executeUpdate(str);
            if(count>=1){
                System.out.println("删除成功");
            }
            else{
                System.out.println("删除失败");
            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //删除gongying
    public static void delete_gongying(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="delete from t_gongying where 产品ID = "+did;

            int count = stat1.executeUpdate(str);
            if(count>=1){
                System.out.println("删除成功");
            }
            else{
                System.out.println("删除失败");
            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //删除商品
    public static void delete_product(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="delete from t_product where 产品ID = "+did;

            int count = stat1.executeUpdate(str);
            if(count>=1){
                System.out.println("删除成功");
            }
            else{
                System.out.println("删除失败");
            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //删除shuyu
    public static void delete_shuyu(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="delete from t_shuyu where 产品ID = "+did;

            int count = stat1.executeUpdate(str);
            if(count>=1){
                System.out.println("删除成功");
            }
            else{
                System.out.println("删除失败");
            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //删除用户
    public static void delete_user(String did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="delete from t_user where 客户ID = "+"'"+did+"'";

            int count = stat1.executeUpdate(str);
            if(count>=1){
                System.out.println("删除成功");
            }
            else{
                System.out.println("删除失败");
            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //删除雇员
    public static void delete_worker(int did) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="delete from t_worker where 雇员ID = "+did;

            int count = stat1.executeUpdate(str);
            if(count>=1){
                System.out.println("删除成功");
            }
            else{
                System.out.println("删除失败");
            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }




    //展示所有用户
    public static void show_all_user() {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select * from t_user where 客户ID is not null ";

            ResultSet res=null;
            res = stat1.executeQuery(str);

            while(res.next()){

                //1234表示表列数，类型和数据库表属性类型相一致，优势：方便计算，如工资涨100可直接输出salary+100
                String id = res.getString(1);
                String ename=res.getString(2);
                String name=res.getString(3);
                String wor=res.getString(4);
                String ads=res.getString(5);
                String city=res.getString(6);
                String area=res.getString(7);
                String cod=res.getString(8);
                String nation=res.getString(9);
                String tel=res.getString(10);
                String cz= res.getString(11);
                String psw=res.getString(12);

                System.out.println(id+","+ename+","+name+","+wor+","+ads+","+city+","+area+","+cod+","+nation+","+tel+","+cz) ;
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //展示所有雇员
    public static void show_all_worker() {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();

            String str="select * from t_worker where 雇员ID is not null ";

            ResultSet res=null;
            res = stat1.executeQuery(str);

            while(res.next()){

                //1234表示表列数，类型和数据库表属性类型相一致，优势：方便计算，如工资涨100可直接输出salary+100
                int id = res.getInt(1);
                String ename=res.getString(2);
                String name=res.getString(3);
                String wor=res.getString(4);
                String zc=res.getString(5);
                String datetime1=res.getString(6);
                String datetime2=res.getString(7);
                String ads=res.getString(8);
                String city=res.getString(9);
                String area=res.getString(10);
                String cod=res.getString(11);
                String nation=res.getString(12);
                String tel=res.getString(13);
                String fj= res.getString(14);
                String zp=res.getString(15);
                String bz=res.getString(16);
                int sj= res.getInt(17);
                String psw=res.getString(18);

                System.out.println(id+","+ename+","+name+","+wor+","+zc+","+datetime1+","+datetime2+","+ads+","+city+","+area+","+cod+","+nation+","+tel+","+fj+","+zp+","+bz+","+sj) ;
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //展示所有供应商
    public static void show_all_provider() {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();


            String str="select* from t_provider where 供应商ID IS NOT NULL ";

            ResultSet res=null;
            res = stat1.executeQuery(str);

            while(res.next()){

                //1234表示表列数，类型和数据库表属性类型相一致，优势：方便计算，如工资涨100可直接输出salary+100
                int id = res.getInt(1);
                String ename=res.getString(2);
                String name=res.getString(3);
                String wor=res.getString(4);
                String ads=res.getString(5);
                String city=res.getString(6);
                String area=res.getString(7);
                String cod=res.getString(8);
                String nation=res.getString(9);
                String tel=res.getString(10);
                String cz= res.getString(11);
                String web=res.getString(12);

                System.out.println(id+","+ename+","+name+","+wor+","+ads+","+city+","+area+","+cod+","+nation+","+tel+","+cz+","+web) ;
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //展示所有领导关系
    public static void show_all_lingdao(int nid) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();


            String str="select 雇员ID from t_lingdao where 上级="+nid;

            ResultSet res=null;
            res = stat1.executeQuery(str);
            int ii=0;
            g_lingdao_len=0;

            while(res.next()){
                //1234表示表列数，类型和数据库表属性类型相一致，优势：方便计算，如工资涨100可直接输出salary+100
                g_lingdao_gyid[ii] = res.getInt(1);
                ii++;
            }
            g_lingdao_len=ii;

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //展示所有供应关系
    public static void show_all_gongying(int nid) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();


            String str="select 产品ID from t_gongying where 供应商ID="+nid;

            ResultSet res=null;
            res = stat1.executeQuery(str);
            int ii=0;
            g_gongying_len=0;

            while(res.next()){
                //1234表示表列数，类型和数据库表属性类型相一致，优势：方便计算，如工资涨100可直接输出salary+100
                g_gongying_cid[ii] = res.getInt(1);
                ii++;
            }
            g_gongying_len=ii;

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //展示所有属于关系
    public static void show_all_shuyu(int nid) {
        Connection conn=null;
        Statement stat1=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            stat1=conn.createStatement();


            String str="select 产品ID from t_shuyu where 类别ID="+nid;

            ResultSet res=null;
            res = stat1.executeQuery(str);
            int ii=0;
            g_shuyu_len=0;

            while(res.next()){
                //1234表示表列数，类型和数据库表属性类型相一致，优势：方便计算，如工资涨100可直接输出salary+100
                g_shuyu_cid[ii] = res.getInt(1);
                ii++;
            }
            g_shuyu_len=ii;

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(stat1!=null){
                try {
                    stat1.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }



    //更新用户信息
    public static String update_user(String kid,String ename,String name,String wor,String ads,String city,String area,String cod,String nation,String tel,String cz,String pw)
    {
        Connection conn=null;
        PreparedStatement pstmt=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn= DriverManager.getConnection(url,user,password);

            ResultSet res=null;

            String sql="update t_user set 客户ID=?,公司名称=?,联系人姓名=?,联系人职务=?,地址=?,城市=?,地区=?,邮政编码=?,国家=?,电话=?,传真=?,psw=? where 客户ID="+kid;

            pstmt=conn.prepareStatement(sql);

            pstmt.setString(1, kid);
            pstmt.setString(2, ename);
            pstmt.setString(3, name);
            pstmt.setString(4,wor);
            pstmt.setString(5,ads);
            pstmt.setString(6, city);
            pstmt.setString(7,area);
            pstmt.setString(8,cod);
            pstmt.setString(9,nation);
            pstmt.setString(10,tel);
            pstmt.setString(11,cz);
            pstmt.setString(12,pw);


            int result=pstmt.executeUpdate();
            System.out.println(String.format("数据库保存了%d个客户", result));
            return kid;
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null){
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
        return kid;
    }

    //更新雇员信息
    public static void update_worker(int nid,String ename,String name,String wor,String zc,String datetime1,String datetime2,String ads,String city,String area,String cod,String nation,String tel,String fj,String zp,String bz,int sj,String pw)
    {
        Connection conn=null;
        PreparedStatement pstmt=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);


            ResultSet res=null;


            String sql="update t_worker set 雇员ID=?,姓氏=?,名字=?,职务=?,尊称=?,出生日期=?,雇用日期=?,地址=?,城市=?,地区=?,邮政编码=?,国家=?,家庭电话=?,分机=?,照片=?,备注=?,上级=?,psw=? where 雇员ID="+nid;
            pstmt=conn.prepareStatement(sql);
//
            pstmt.setInt(1, nid);
            pstmt.setString(2, ename);
            pstmt.setString(3, name);
            pstmt.setString(4,wor);
            pstmt.setString(5, zc);
            pstmt.setString(6, datetime1);
            pstmt.setString(7,datetime2);
            pstmt.setString(8, ads);
            pstmt.setString(9, city);
            pstmt.setString(10,area);
            pstmt.setString(11,cod);
            pstmt.setString(12,nation);
            pstmt.setString(13,tel);
            pstmt.setString(14,fj);
            pstmt.setString(15,zp);
            pstmt.setString(16,bz);
            if(sj==0){
                pstmt.setString(17,null);
            }
            else{
                pstmt.setInt(17,sj);
            }
            pstmt.setString(18,pw);


            int result=pstmt.executeUpdate();
            System.out.println(String.format("数据库保存了%d个雇员", result));
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null){
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }


    //更新类别信息
    public static void update_class(int nid,String cname,String shuoming,String tp) {
        Connection conn=null;
        PreparedStatement pstmt=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn= DriverManager.getConnection(url,user,password);

            ResultSet res=null;


            String sql="update t_class set 类别ID=?,类别名称=?,说明=? where 类别ID="+nid;
            pstmt=conn.prepareStatement(sql);

            pstmt.setInt(1, nid);
            pstmt.setString(2, cname);
            pstmt.setString(3, shuoming);
//          pstmt.setString(4,tp);
            int result=pstmt.executeUpdate();

//            image_to_hex(tp,nid);

            System.out.println(String.format("数据库保存了%d个类别", result));
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null){
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //更新产品信息
    public static void update_product(int nid,String ename,String sl,String mon,Short rel,Short dgl,Short zdgl,Boolean zz,int gid,int cid) {
        Connection conn=null;
        PreparedStatement pstmt=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);

            ResultSet res=null;

            String sql="update t_product set 产品ID=?,产品名称=?,单位数量=?,单价=?,库存量=?,订购量=?,再订购量=?,中止=? where 产品ID ="+nid;
            pstmt=conn.prepareStatement(sql);

            pstmt.setInt(1, nid);
            pstmt.setString(2, ename);
            pstmt.setString(3, sl);
            pstmt.setString(4,mon);
            pstmt.setShort(5, rel);
            pstmt.setShort(6, dgl);
            pstmt.setShort(7,zdgl);
            pstmt.setBoolean(8, zz);

            add_gongying(nid,gid);
            add_shuyu(nid,cid);

            int result=pstmt.executeUpdate();
            System.out.println(String.format("数据库保存了%d个产品", result));
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null){
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //更新供应商信息
    public static void update_provider(int nid,String ename,String name,String wor,String ads,String city,String area,String cod,String nation,String tel,String cz,String web)
    {
        Connection conn=null;
        PreparedStatement pstmt=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn=DriverManager.getConnection(url,user,password);


            ResultSet res=null;

            String str="select max(供应商ID) cd from t_provider";
            pstmt=conn.prepareStatement(str);
            res = pstmt.executeQuery();

            String sql="update t_provider set 供应商ID=?,公司名称=?,联系人姓名=?,联系人职务=?,地址=?,城市=?,地区=?,邮政编码=?,国家=?,电话=?,传真=?,主页=?";
            pstmt=conn.prepareStatement(sql);

            pstmt.setInt(1, nid);
            pstmt.setString(2, ename);
            pstmt.setString(3, name);
            pstmt.setString(4,wor);
            pstmt.setString(5, ads);
            pstmt.setString(6, city);
            pstmt.setString(7,area);
            pstmt.setString(8, cod);
            pstmt.setString(9, nation);
            pstmt.setString(10,tel);
            pstmt.setString(11,cz);
            pstmt.setString(12,web);

            int result=pstmt.executeUpdate();
            System.out.println(String.format("数据库保存了%d个供应商", result));
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null){
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //更新shuyu信息
    public static void update_shuyu(int pid,int cid) {
        Connection conn=null;
        PreparedStatement pstmt=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn = DriverManager.getConnection(url, user, password);

            ResultSet res = null;

            String sql="update t_shuyu set 产品ID="+pid+",类别ID="+cid+"where 产品ID ="+pid;

            pstmt=conn.prepareStatement(sql);
            int result=pstmt.executeUpdate();
            System.out.println(String.format("数据库保存了%d个属于信息", result));
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null){
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }

    //更新gongying信息
    public static void update_gongying(int pid,int cid) {
        Connection conn=null;
        PreparedStatement pstmt=null;
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
            String user = "sa";
            String password = "123456";
            conn = DriverManager.getConnection(url, user, password);

            ResultSet res = null;

            String sql="update t_gongying set 产品ID="+pid+",供应商ID="+cid+"where 产品ID ="+pid;

            pstmt=conn.prepareStatement(sql);
            int result=pstmt.executeUpdate();
            System.out.println(String.format("数据库保存了%d个供应信息", result));
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
            if(pstmt!=null){
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    // TODO 自动生成的 catch 块
                    e.printStackTrace();
                }
            }
        }
    }




    //自己图片转换方法
    public static void image_to_hex(String imagePath,int cid) {
        //    String imagePath = "C:\\Users\\rcw25\\Desktop\\picture\\hx.jpg";
        String outputFilePath = "C:\\Users\\rcw25\\Desktop\\picture\\1.txt";
        //    int cid=8;
        try {
            // 将图片转换为十六进制格式并保存到文本文件
            convertImageToHex(imagePath, outputFilePath);
            //更新到数据库
            updat(outputFilePath,cid);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void convertImageToHex(String imagePath, String outputFilePath) throws IOException {
        try (BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(outputFilePath))) {
            FileInputStream fis = new FileInputStream(imagePath);
            int byteRead;
            while ((byteRead = fis.read()) != -1) {
                String hex = String.format("%02X", byteRead);
                bos.write(hex.getBytes());
            }
        }
    }

    public static void updat(String filePath,int cid) {
        String url = "jdbc:sqlserver://localhost:1433;DatabaseName=csharpdatabase";
        String username = "sa";
        String password = "123456";

        String insertQuery = "UPDATE t_class SET 图片=? where 类别ID =?"; // 替换为你的表名和字段名

        try {
            // 连接到数据库
            Connection connection = DriverManager.getConnection(url, username, password);

            // 读取十六进制数据文件
            String hexString = readHexStringFromFile(filePath);

            // 转换十六进制字符串为字节数组
            byte[] imageData = hexStringToByteArray(hexString);

            // 执行插入操作
            PreparedStatement statement = connection.prepareStatement(insertQuery);
            statement.setBytes(1, imageData);
            statement.setInt(2, cid);
            statement.executeUpdate();

            System.out.println("图像数据已成功插入到数据库中");

            // 关闭连接
            statement.close();
            connection.close();
        } catch (SQLException | IOException e) {
            e.printStackTrace();
        }
    }

    // 从文件中读取十六进制字符串
    private static String readHexStringFromFile(String filePath) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader reader = new BufferedReader(new FileReader(filePath));
        String line;
        while ((line = reader.readLine()) != null) {
            sb.append(line);
        }
        reader.close();
        return sb.toString();
    }

    // 将十六进制字符串转换为字节数组
    private static byte[] hexStringToByteArray(String hexString) {
        int len = hexString.length();
        byte[] byteArray = new byte[len / 2];
        for (int i = 0; i < len; i += 2) {
            byteArray[i / 2] = (byte) ((Character.digit(hexString.charAt(i), 16) << 4)
                    + Character.digit(hexString.charAt(i + 1), 16));
        }
        return byteArray;
    }


    //老师图片转换方法，从数据库中读取二进制图片文件，转化成png保存在电脑路径上
    public static void db_to_png(String outputFilePath,int cid) {
        String connectionString = "jdbc:sqlserver://localhost:1433;databaseName=csharpdatabase;user=sa;password=123456";
        String tableName = "t_class";
        String columnName = "图片";
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
