from flask import Flask, render_template, request
import cx_Oracle
from db_config import get_connection  # Ensure correct implementation

app = Flask(__name__)

@app.route('/')
def query_page():
    return render_template('query.html', columns=None, data=None, error=None)

@app.route('/query', methods=['POST'])
def execute_query():
    conn = get_connection()
    if conn is None:
        return render_template('query.html', error="Database connection failed.", columns=None, data=None)

    cursor = conn.cursor()
    try:
        sql_query = request.form.get('query')
        if not sql_query:
            return render_template('query.html', error="Query cannot be empty.", columns=None, data=None)

        cursor.execute(sql_query)
        columns = [col[0] for col in cursor.description]  # Extract column names
        results = cursor.fetchall()
        data = [dict(zip(columns, row)) for row in results]  # Convert rows into dictionaries
        
    except Exception as e:
        return render_template('query.html', error=str(e), columns=None, data=None)
    finally:
        cursor.close()
        conn.close()

    return render_template('query.html', columns=columns, data=data, error=None)

if __name__ == '__main__':
    app.run(debug=True)
