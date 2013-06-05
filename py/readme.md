myre ==> baidu
myre2 ==> diandian

myresulte.txt ==> time stmp 2 utc

result ==> top queries


use xx.encode("utf8") instead of unicode(xx)

db finished

Error: no such table: Cars
sqlite3 xxx
sqlite3> some command

SQLite is technically thread safe, but a write operation locks the entire database [1]:
- Any resultset being step()'d through uses a shared read-only lock. 
- Any insert/update being executed requires an exclusive write lock.

Docs: "while the database supports concurrent read access, only one user may write to it at a time. This is because a filesystem lock is placed on the file during write operations. This is an important point to bear in mind with multi-threaded applications"
