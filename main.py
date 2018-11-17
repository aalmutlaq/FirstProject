import psycopg2
import logging
import pickle

# Define varibales with the questions need to be answered
q1 = ('1-What are the most popular three articles of all time?')
q2= ("2-Who are the most popular article authors of all time?")
q3=("3-On which days did more than 1% of requests lead to errors?")

# Create DB connection 
conn = psycopg2.connect("dbname=news")
#define cursor 
cursor1 = conn.cursor()
#execute the cursor1 to answer Q1 
cursor1.execute(
    "SELECT a.title AS Article_Title, COUNT(*) no_of_views "
    "FROM log l, articles a WHERE a.slug = substring(l.path,10,100) "
    "AND l.status='200 OK' AND UPPER(l.path) LIKE'%ARTICLE%' "
    "GROUP BY a.title ORDER BY No_of_Views DESC LIMIT 3;"
                )   
# assgin varible a1 with cursor1 and fetch the data                
a1 = cursor1.fetchall()
# print the first question 
print(q1)
# print the first answers
print(a1)



#define cursor 
cursor2 = conn.cursor()
#execute the cursor2 to answer Q2
cursor2.execute(
    "SELECT (SELECT name FROM authors WHERE id =a.author) AS Author, "
     "COUNT(*) COUNT FROM log l, articles a "
    "WHERE a.slug = SUBSTRING(l.path,10,100) "
    "AND l.status='200 OK' AND UPPER(l.path) LIKE '%ARTICLE%' "
    "GROUP BY Author " 
    "ORDER BY count DESC;"
                )
# assgin varible a2 with cursor1 and fetch the data 
a2 = cursor2.fetchall()
# print the second question 
print(q2)
# print the second answers
print(a2)


#define cursor 
cursor3 = conn.cursor()
#execute the cursor2 to answer Q2
cursor3.execute(
    "SELECT CAST(date AS text) AS date, per ||'%' percentage FROM(SELECT date, "
    "ROUND((CAST(b.falid as decimal)/cast(b.pass AS DECIMAL)*100),2)per, b.falid,b.pass "
    "FROM (SELECT t.date, t.falid,t.pass FROM ("
    "SELECT DATE(time) date, SUM(CASE  WHEN status = '200 OK' THEN 1 ELSE 0 END) pass, "
    "SUM(CASE WHEN status ='404 NOT FOUND' THEN 1 ELSE 0 END) falid FROM log "
    "GROUP BY DATE(time))t)b)c WHERE per >=1 ;"
)

a3 = cursor3.fetchall()
print(q3)
print(a3)

conn.close() 



saveFile = open('results.txt', 'w')
saveFile.write(str(q1)+'\n'+str(a1)+'\n')
saveFile.write(str(q2)+'\n'+str(a2) +'\n')
saveFile.write(str(q3)+'\n'+str(a3) +'\n')
saveFile.close()   