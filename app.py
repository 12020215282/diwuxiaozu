from flask import Flask,render_template,request
import pymysql

app = Flask (__name__)

mysql_host = "172.18.0.2"
mysql_user = "root"
mysql_pwd = "123456"
mysql_db_name = "dmeo"
# 封装SQL语句函数
def func(sql,m='r'):
    py =pymysql.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_pwd,
        database=mysql_db_name)
    cursor = py.cursor ()
    try:
        cursor.execute (sql)
        if m == 'r':
            data = cursor.fetchall ()
        elif m == 'w':
            py.commit ()
            data = cursor.rowcount
    except:
        data = False
        py.rollback ()
    py.close ()
    return data


# 首页,将mysql中表的值读出并传到网页----查
@app.route ('/')
def index():
    data = func ('select * from user_info')
    for i in data:
        print(i)

    return render_template ('sqldata.html',userlist=data)


# 返回到添加操作的界面
@app.route ("/add/")
def ad():
    return render_template ('add.html')


# 接受添加的数据,写入数据库----增
@app.route ("/adds/",methods=["POST"])  # 注意post大写,因为post是通过form.data传数据所以下面用request.form
def adds():
    data = dict (request.form)
    print (data)
    sql = "insert into user_info values ('{id}','{name}','{age}','{sex}','{phone}')".format (**data)
    res = func (sql,m='w')
    if res:
        return '<script>alert("添加成功");location.href="/";</script>'
    else:
        return '<script>alert("添加失败");location.href="/";</script>'


# 返回到更改界面
@app.route ('/cha')
def ch():
    idd = request.args.get ('id')
    data = func (f'select * from user_info where id={idd}')
    return render_template ('cha.html',userlist=data)


# 检察更改的数据并更新数据库----改
@app.route ('/chas',methods=["POST"])
def chas():
    data = dict (request.form)
    res = func ("update user_info set name='{name}',age='{age}',sex='{sex}',phone='{phone}' where id={id}".format (**data),
                m='w')
    if res:
        return '<script>alert("更新成功");location.href="/";</script>'
    else:
        return '<script>alert("未更新");location.href="/";</script>'


# 删除数据----删
@app.route ('/del')
def de():
    id = request.args.get ('id')
    res = func (f'delete from user_info where id={id}',m='w')
    if res:
        return '<script>alert("删除成功");location.href="/";</script>'
    else:
        return '<script>alert("删除失败");location.href="/";</script>'


# 运行
if __name__ == '__main__':
    app.run (debug=True,host='0.0.0.0',port='5000')


