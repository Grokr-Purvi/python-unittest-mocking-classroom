import psycopg2 as pg2


class DbHelper:
    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        conn = pg2.connect(database="Employee", user="postgres",password="postgres", host="localhost")
        cur = conn.cursor()


        query1 = '''
                SELECT MAX(salary) FROM
                employee_data
                ;
                '''

        cur.execute(query1)
        # cur.commit()
        data = cur.fetchone()
        conn.close()

        return data

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        conn = pg2.connect(database="Employee", user="postgres",password="postgres", host="localhost")
        cur = conn.cursor()


        query1 = '''
                SELECT MIN(salary) FROM
                employee_data
                ;
                '''

        cur.execute(query1)
        # cur.commit()
        data = cur.fetchone()
        conn.close()

        return data

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)