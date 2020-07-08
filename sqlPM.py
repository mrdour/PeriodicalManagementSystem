import pymysql
import time
import string

class Sqloperation:
    def __init__(self):
        # connect to database
        self.db = pymysql.connect("192.168.11.190", "adminer", "mysql", "periodicalDB")
        # create cursor
        self.cursor = self.db.cursor()
    def __del__(self):
        # disconnect database
        self.db.close()
    def inquiry_content_by_kw(self,kwd):
        'inquiry contents of periodical by keywords'
        self.cursor.execute(r""" SELECT * FROM `content_table`
                                WHERE `Ct_keyword1` like '%{0}%'
                                OR `Ct_keyword2` like '%{0}%'
                                OR `Ct_keyword3` like '%{0}%'
                                OR `Ct_keyword4` like '%{0}%'
                                OR `Ct_keyword5` like '%{0}%'""".format(kwd))
        return self.cursor.fetchall()
    def inquiry_content_by_au(self,auname):
        'inquiry contents of periodical by auther'
        self.cursor.execute(r""" SELECT * FROM `content_table`
                                WHERE `Ct_author` like '%{}%'""".format(auname))
        return self.cursor.fetchall()
    def inquiry_content_by_tt(self,title):
        'inquiry contents of periodical by title'
        self.cursor.execute(r""" SELECT * FROM `content_table`
                                WHERE `Ct_title` like '%{}%'""".format(title))
        return self.cursor.fetchall()
    def inquiry_register(self,pname):
        'inquiry registed periodical list'
        self.cursor.execute(r""" SELECT * FROM `register_table`
                                WHERE R_qkmc like '%{}%'""".format(pname))
        return self.cursor.fetchall()
    def inquirysubscription(self):
        'inquiry periodical subscription list'
        self.cursor.execute(r""" SELECT * FROM `subscription_table`""")
        return self.cursor.fetchall()
    def inquiry_pinfo(self,pname):
        'inquiry periodical info'
        self.cursor.execute(r""" SELECT * FROM catalog_table 
                        WHERE Cg_qkmc like '%{}%'""".format(pname))
        return self.cursor.fetchall()  
    def inquiry_pbinfo(self,pname):
        'inquiry periodical borrowed info'
        self.cursor.execute(r""" SELECT * FROM borrow_table 
                        WHERE B_qkmc like '%{}%'""".format(pname))
        return self.cursor.fetchall()
    def inquiry_ubinfo(self,uname):
        'inquiry user borrow info'
        self.cursor.execute(r""" SELECT * FROM borrow_table 
                        WHERE `B_gh` like '{}'""".format(uname))
        return self.cursor.fetchall()

    def addF(self):
        try:
            self.cursor.execute("""INSERT INTO 
                        (,)
                            VALUES (,)""")
            self.db.commit()
        except:
            self.db.rollback()
    def subscript(self,pname,yfdm,nf):
        try:
            self.cursor.execute(r"""INSERT INTO `subscription_table`
                        (`S_qkmc`,`S_yfdm`, `S_zdnf`)
                            VALUES ('{}', '{}', {})""".format(pname,yfdm,nf))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
    def addcontent(self,pname,year,volume,issue,title,author,page,k1,k2,k3,k4,k5):
        try:
            self.cursor.execute(r"""INSERT INTO `content_table`
                        (`Ct_qkmc`, `Ct_year`, `Ct_volume`, `Ct_issue`,
                        `Ct_title`,`Ct_author`,`Ct_page`,`Ct_keyword1`,
                        `Ct_keyword2`,`Ct_keyword3`,`Ct_keyword4`,`Ct_keyword5`)
                            VALUES ('{}', {}, {}, {}, '{}','{}','{}','{}','{}','{}','{}','{}')
                            """.format(pname,year,volume,issue,title,author,page,k1,k2,k3,k4,k5))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
    def register(self,pname,year,volume,issue):
        try:
            self.cursor.execute(r"""INSERT INTO `register_table`
                        (`R_qkmc`, `R_year`, `R_volume`, `R_issue`)
                            VALUES ('{}', {}, {}, {})""".format(pname,year,volume,issue))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
    def addcatalog(self,pname,cn,issn,yfdm,cbzq,cbd,cbdw):
        try:
            self.cursor.execute(r"""INSERT INTO `catalog_table`
                        (`Cg_qkmc`,`Cg_CN`, `Cg_ISSN`, `Cg_yfdm`, `Cg_cbzq`,`Cg_cbd`,`Cg_zbdw`)
                            VALUES ('{}', '{}', '{}', '{}','{}','{}','{}')
                            """.format(pname,cn,issn,yfdm,cbzq,cbd,cbdw))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
    def lend(self,uname,pname,year,volume,issue):
        try:
            self.cursor.execute(r"""INSERT INTO `borrow_table`
                            (`B_gh`, `B_qkmc`, `B_year`, `B_volume`, `B_issue`, `B_jyrq`)
                                VALUES ('{}', '{}', {}, {}, {}, '{}')
                            """.format(uname,pname,year,volume,issue,r'{}.{:02}.{:02}'.format(time.localtime()[0],time.localtime()[1],time.localtime()[2])))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
    def addadmin(self,zh,passwd):
        try:
            self.cursor.execute(r"""INSERT INTO `administrator_table`
                        (Admin_zh,Admin_password)
                            VALUES ('{}', '{}')""".format(zh,passwd))
            self.db.commit()
        except:
            self.db.rollback()
    def adduser(self,zh,passwd):
        try:
            self.cursor.execute(r"""INSERT INTO `user_table`
                        (User_gh,User_password)
                            VALUES ('{}', '{}')""".format(zh,passwd))
            self.db.commit()
        except:
            self.db.rollback()

    def returnp(self,pname,year,volume,issue):
        try:
            self.cursor.execute(r""" UPDATE `borrow_table`
                        SET `B_ghrq` = '{}'
                        WHERE `B_qkmc`='{}'
                        AND `B_year`={}
                        AND `B_volume`={}
                        AND `B_issue`={} 
                        """.format(r'{}.{:02}.{:02}'.format(time.localtime()[0],time.localtime()[1],time.localtime()[2]),pname,year,volume,issue))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
    def update_admin_passwd(self,username,newp):
        # update the user password
        try:
            self.cursor.execute(r"""UPDATE `administrator_table` 
                        SET `Admin_password` = '{}' 
                        WHERE `Admin_zh` = '{}'""".format(newp,username))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
        return False
    def update_user_passwd(self,uname,newp):
        try:
            self.cursor.execute(r"""UPDATE `user_table` 
            SET `User_password` = '{}' 
            WHERE `User_gh` like '{}'""".format(newp,uname))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
    def bookp(self,bpname,uname,year,volume,issue):
        try:
            self.cursor.execute(r"""UPDATE `borrow_table` 
                        SET `B_ydyh` = '{}' 
                        WHERE `B_qkmc` like '{}'
                        AND `B_year`= {}
                        AND `B_volume`= {}
                        AND `B_issue`= {}""".format(uname,bpname,year,volume,issue))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def delF(self):
        try:
            self.cursor.execute(r""" DELETE FROM 
                        WHERE
                        AND
                        """)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
    def delcontent(self,pname,pyear,pvolume,pissue,title,author,page):
        try:
            self.cursor.execute(r""" DELETE FROM `content_table`
                        WHERE `Ct_qkmc` like '{}'
                        AND `Ct_year` like {}
                        AND `Ct_volume` like {}
                        AND `Ct_issue` like {}
                        AND `Ct_title` like '{}'
                        AND `Ct_author` like '{}'
                        AND `Ct_page` like '{}'
                        """.format(pname,pyear,pvolume,pissue,title,author,page))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
    def delsub(self,pname,pmail,syear):
        try:
            self.cursor.execute(r""" DELETE FROM `subscription_table`
                        WHERE `S_qkmc` like '{}'
                        AND `S_yfdm` like '{}'
                        AND `S_zdnf` like '{}'
                        """.format(pname,pmail,syear))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
    def is_admin(self,uname):
        'if admin'
        self.cursor.execute(r""" SELECT `Admin_zh`
                        FROM `administrator_table` 
                        WHERE `Admin_zh` like '{}'""".format(uname))
        if self.cursor.fetchone():return True
        return False
    def is_user_exist(self,uname):
        if self.is_admin(uname):return True
        else:
            self.cursor.execute(r""" SELECT `User_gh`
                            FROM `user_table` 
                            WHERE `User_gh` like '{}'""".format(uname))
            if self.cursor.fetchone():return True
            return False
    def is_pass_match(self,uname,passwd):
        if self.is_user_exist(uname):
            if self.is_admin(uname):
                self.cursor.execute(r""" SELECT `Admin_password`
                            FROM `administrator_table` 
                            WHERE `Admin_zh` like '{}'""".format(uname))
                if passwd==self.cursor.fetchone()[0]:
                    return True
            else:
                self.cursor.execute(r""" SELECT `User_password`
                                FROM `user_table` 
                                WHERE `User_gh` like '{}'""".format(uname))
                if passwd==self.cursor.fetchone()[0]:
                    return True
        return False
    def checkidformat(self,id):
        if id.__len__()!=9:
            return False
        elif not string.ascii_letters.count(id[0]):
            return False
        return True
    def checkpassformat(self,passwd):
        if not passwd:
            return False
        for letter in passwd:
            if letter==' ':
                return False
        return True
    def checkinputcatalog(self,cn,issn,mail,period):
        # CN XX-XXXX
        # ISSN XXXX-XXXX
        # mail xx-xxx or xx-xx
        # 旬刊，半月刊，月刊，双月刊，季刊，半年刊，年刊
        if cn.find('/')==-1 or cn.find('/')==0 or cn.find('/')==len(cn):
            return "CN号格式（XX-XXXX/Y；X为数字,Y为1-2位字母）不正确"
        cnpart=cn.split('/')
        cn=cnpart[0]
        cn1=cnpart[1]
        for _ in range(7):
            if _ !=2:
                if not string.digits.count(cn[_]):
                    return "CN号格式（XX-XXXX/Y；X为数字,Y为1-2位字母）不正确"
            elif cn[_]!='-':
                return "CN号格式（XX-XXXX/Y；X为数字,Y为1-2位字母）不正确"
        if len(cn1)<1:
            return "CN号格式（XX-XXXX/Y；X为数字,Y为1-2位字母）不正确"
        for _ in range(len(cn1)):
            if not string.ascii_letters.count(cn1[_]):
                return "CN号格式（XX-XXXX/Y；X为数字,Y为1-2位字母）不正确"
        # issn
        if len(issn)!=9:
            return "ISSN号格式（XXXX-XXXX；X为数字,Y为1-2位字母）不正确"
        else:
            for _ in range(9):
                if _ !=4:
                    if not string.digits.count(issn[_]):
                        return "ISSN号格式（XXXX-XXXX；X为数字）不正确"
                elif issn[_]!='-':
                    return "ISSN号格式（XXXX-XXXX；X为数字）不正确"
        if len(mail)<3 or len(mail)>7:
            return "邮发代号格式（X1-X2;X1为1-2位数字,X2为1-3位数字）不正确"
        else:
            if mail.find('-') ==-1 or mail.find('-') ==0 or mail.find('-') ==len(mail):
                return "邮发代号格式（X1-X2;X1为1-2位数字,X2为1-3位数字）不正确"
            codes=mail.split('-')
            for _ in range(codes.__len__()):
                for i in codes[_]:
                    if not string.digits.count(i):
                        return "邮发代号格式（X1-X2;X1为1-2位数字,X2为1-3位数字）不正确"
        if period!='旬刊' and period!='半月刊' and period!='月刊' and period!='双月刊' and period!='季刊' and period!='半年刊' and period!='年刊':
            return "周期只能为：旬刊，半月刊，月刊，双月刊，季刊，半年刊，年刊其中一种"
        return False
    def checkinputregister(self,pyear):
        if len(pyear)!=4:
            return "年份格式不正确"
        for _ in range(4):
            if not string.digits.count(pyear[_]):
                return "年份格式不正确"
        return False
    def checkinputcontent(self,pyear,page):
        # page x*-x*
        if len(pyear)!=4:
            return "年份格式不正确"
        for _ in range(4):
            if not string.digits.count(pyear[_]):
                return "年份格式不正确"
        if page.find('-')!=-1:
            if page.find('-') ==-1 or page.find('-') ==0 or page.find('-') ==len(page):
                return "页码格式（数字1-数字2或数字1~数字2;且数字2>数字1）不正确"
            pages=page.split('-')
            for p1 in pages:
                for p2 in p1:
                    if not string.digits.count(p2):
                        return "页码格式（数字1-数字2或数字1~数字2;且数字2>数字1）不正确"
            p1=pages[0]
            p2=pages[1]
            if int(p2)<int(p1):
                return "页码格式（数字1-数字2或数字1~数字2;且数字2>数字1）不正确"
        elif page.find('~')!=-1:
            if page.find('~') ==-1 or page.find('~') ==0 or page.find('~') ==len(page):
                return "页码格式（数字1-数字2或数字1~数字2;且数字2>数字1）不正确"
            pages=page.split('~')
            for p1 in pages:
                for p2 in p1:
                    if not string.digits.count(p2):
                        return "页码格式（数字1-数字2或数字1~数字2;且数字2>数字1）不正确"
            p1=pages[0]
            p2=pages[1]
            if int(p2)<int(p1):
                return "页码格式（数字1-数字2或数字1~数字2;且数字2>数字1）不正确"
        else:return "页码格式（数字1-数字2或数字1~数字2;且数字2>数字1）不正确"
        return False
    def checkinputsub(self,mail,syear):
        # mail x-x
        if len(mail)<3 or len(mail)>7:
            return "邮发代号格式（X1-X2;X1为1-2位数字,X2为1-3位数字）不正确"
        else:
            if mail.find('-') ==-1 or mail.find('-') ==0 or mail.find('-') ==len(mail):
                return "邮发代号格式（X1-X2;X1为1-2位数字,X2为1-3位数字）不正确"
            codes=mail.split('-')
            for _ in range(codes.__len__()):
                for i in codes[_]:
                    if not string.digits.count(i):
                        return "邮发代号格式（X1-X2;X1为1-2位数字,X2为1-3位数字）不正确"
        if len(syear)!=4:
            return "年份格式不正确"
        for _ in range(4):
            if not string.digits.count(syear[_]):
                return "年份格式不正确"
        return False