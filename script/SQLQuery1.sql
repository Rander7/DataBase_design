use csharpdatabase

go

INSERT INTO t_user 
SELECT *
FROM i_user
WHERE i_user.客户ID IS NOT NULL 

delete from i_user


INSERT INTO t_worker 
SELECT *
FROM i_worker
WHERE i_worker.雇员ID IS NOT NULL

delete from i_worker


INSERT INTO t_product 
SELECT *
FROM i_product
WHERE i_product.产品ID IS NOT NULL

delete from i_product



INSERT INTO t_order(订单ID,订购日期,发货日期,到货日期,货款确认日期,运货费,货主名称,货主地址,货主城市,货主地区,货主邮政编码,货主国家,折扣id,取消)
SELECT 订单ID,订购日期,发货日期,到货日期,货款确认日期,运货费,货主名称,货主地址,货主城市,货主地区,货主邮政编码,货主国家,折扣id,取消
FROM i_order
WHERE i_order.订单ID IS NOT NULL

delete from i_order


INSERT INTO t_odetails
SELECT *
FROM i_odetails
WHERE i_odetails.订单ID IS NOT NULL

delete from i_odetails


INSERT INTO t_provider
SELECT *
FROM i_provider
WHERE i_provider.供应商ID IS NOT NULL

delete from i_provider


INSERT INTO t_class(类别ID,类别名称,说明)
SELECT 类别ID,类别名称,说明
FROM i_class
WHERE i_class.类别ID IS NOT NULL

delete from i_class


