from flask import Flask, render_template, url_for, request, redirect
from models.budget_manager import BudgetManager, InvalidExpenseError

app = Flask(__name__)

budget_manager = BudgetManager()

@app.route('/')
def home():
    return render_template('index.html', expenses=budget_manager.expenses)

@app.route('/add', methods=['GET','POST'])
def create_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        date = request.form['date']
        try:
            budget_manager.add_expense(description, amount, date)
            return redirect(url_for("home"))
        except InvalidExpenseError as err:
            pass
        budget_manager.add_expense(description, amount, date)
        return redirect(url_for('home'))
    
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET','POST'])
def update_expense(id):
    if request.method == 'GET':
        expense = budget_manager.get_expense(id)
        return render_template('edit.html', expense=expense)
    
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        date = request.form['date']
        budget_manager.update_expense(id, description, amount, date)
        return redirect(url_for('home'))


    
@app.route('/delete/<int:id>', methods=['POST'])
def delete_expense(id):
    budget_manager.remove_expense(id)
    return redirect(url_for('home'))

@app.route('/my-list')
def show_my_budget():
    return render_template('budget.html', expenses=budget_manager.expenses)

if __name__ == '__main__':
    app.run(debug=True)

