// Add income source
function addIncome() {
    const incomeList = document.getElementById('incomeList');
    const newIncome = document.createElement('div');
    newIncome.className = 'income-item dynamic-item';
    newIncome.innerHTML = `
        <input type="text" name="income_source[]" placeholder="Source (e.g., Salary)" required>
        <input type="number" name="income_amount[]" placeholder="Amount" step="0.01" required>
        <select name="income_frequency[]" required>
            <option value="">Select Frequency</option>
            <option value="monthly">Monthly</option>
            <option value="bi-weekly">Bi-Weekly</option>
            <option value="yearly">Yearly</option>
        </select>
        <button type="button" class="btn-remove" onclick="removeItem(this)">✕</button>
    `;
    incomeList.appendChild(newIncome);
}

// Add expense
function addExpense() {
    const expenseList = document.getElementById('expenseList');
    const newExpense = document.createElement('div');
    newExpense.className = 'expense-item dynamic-item';
    newExpense.innerHTML = `
        <input type="text" name="expense_category[]" placeholder="Category (e.g., Rent)" required>
        <input type="number" name="expense_amount[]" placeholder="Amount" step="0.01" required>
        <select name="expense_frequency[]" required>
            <option value="">Select Frequency</option>
            <option value="monthly">Monthly</option>
            <option value="bi-weekly">Bi-Weekly</option>
            <option value="yearly">Yearly</option>
        </select>
        <label class="checkbox-label">
            <input type="checkbox" name="expense_essential[]" value="true">
            Essential
        </label>
        <button type="button" class="btn-remove" onclick="removeItem(this)">✕</button>
    `;
    expenseList.appendChild(newExpense);
}

// Add debt
function addDebt() {
    const debtList = document.getElementById('debtList');
    const newDebt = document.createElement('div');
    newDebt.className = 'debt-item dynamic-item';
    newDebt.innerHTML = `
        <input type="text" name="debt_type[]" placeholder="Type (e.g., Credit Card)" required>
        <input type="number" name="debt_amount[]" placeholder="Amount" step="0.01" required>
        <input type="number" name="debt_interest[]" placeholder="Interest Rate %" step="0.01" required>
        <input type="number" name="debt_minimum[]" placeholder="Minimum Payment" step="0.01" required>
        <button type="button" class="btn-remove" onclick="removeItem(this)">✕</button>
    `;
    debtList.appendChild(newDebt);
}

// Remove item
function removeItem(button) {
    const item = button.parentElement;
    const parent = item.parentElement;
    
    // Don't remove if it's the last item
    if (parent.children.length > 1) {
        item.remove();
    } else {
        alert('You must have at least one item in each section.');
    }
}

// Reset form
function resetForm() {
    document.getElementById('financialForm').reset();
    document.getElementById('results').classList.add('hidden');
    document.getElementById('financialForm').classList.remove('hidden');
    
    // Reset to single item in each section
    document.getElementById('incomeList').innerHTML = `
        <div class="income-item dynamic-item">
            <input type="text" name="income_source[]" placeholder="Source (e.g., Salary)" required>
            <input type="number" name="income_amount[]" placeholder="Amount" step="0.01" required>
            <select name="income_frequency[]" required>
                <option value="">Select Frequency</option>
                <option value="monthly">Monthly</option>
                <option value="bi-weekly">Bi-Weekly</option>
                <option value="yearly">Yearly</option>
            </select>
            <button type="button" class="btn-remove" onclick="removeItem(this)">✕</button>
        </div>
    `;
    
    document.getElementById('expenseList').innerHTML = `
        <div class="expense-item dynamic-item">
            <input type="text" name="expense_category[]" placeholder="Category (e.g., Rent)" required>
            <input type="number" name="expense_amount[]" placeholder="Amount" step="0.01" required>
            <select name="expense_frequency[]" required>
                <option value="">Select Frequency</option>
                <option value="monthly">Monthly</option>
                <option value="bi-weekly">Bi-Weekly</option>
                <option value="yearly">Yearly</option>
            </select>
            <label class="checkbox-label">
                <input type="checkbox" name="expense_essential[]" value="true">
                Essential
            </label>
            <button type="button" class="btn-remove" onclick="removeItem(this)">✕</button>
        </div>
    `;
    
    document.getElementById('debtList').innerHTML = `
        <div class="debt-item dynamic-item">
            <input type="text" name="debt_type[]" placeholder="Type (e.g., Credit Card)" required>
            <input type="number" name="debt_amount[]" placeholder="Amount" step="0.01" required>
            <input type="number" name="debt_interest[]" placeholder="Interest Rate %" step="0.01" required>
            <input type="number" name="debt_minimum[]" placeholder="Minimum Payment" step="0.01" required>
            <button type="button" class="btn-remove" onclick="removeItem(this)">✕</button>
        </div>
    `;
}

// Handle form submission
document.getElementById('financialForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    
    // Build the financial profile object
    const financialProfile = {
        monthly_income: [],
        monthly_expenses: [],
        debts: [],
        savings: parseFloat(formData.get('savings')) || 0,
        emergency_fund: parseFloat(formData.get('emergency_fund')) || 0,
        retirement_savings: parseFloat(formData.get('retirement_savings')) || 0,
        credit_score: formData.get('credit_score') ? parseInt(formData.get('credit_score')) : null
    };
    
    // Collect income data
    const incomeSources = formData.getAll('income_source[]');
    const incomeAmounts = formData.getAll('income_amount[]');
    const incomeFrequencies = formData.getAll('income_frequency[]');
    
    for (let i = 0; i < incomeSources.length; i++) {
        if (incomeSources[i] && incomeAmounts[i] && incomeFrequencies[i]) {
            financialProfile.monthly_income.push({
                source: incomeSources[i],
                amount: parseFloat(incomeAmounts[i]),
                frequency: incomeFrequencies[i]
            });
        }
    }
    
    // Collect expense data
    const expenseCategories = formData.getAll('expense_category[]');
    const expenseAmounts = formData.getAll('expense_amount[]');
    const expenseFrequencies = formData.getAll('expense_frequency[]');
    const expenseEssential = formData.getAll('expense_essential[]');
    
    for (let i = 0; i < expenseCategories.length; i++) {
        if (expenseCategories[i] && expenseAmounts[i] && expenseFrequencies[i]) {
            financialProfile.monthly_expenses.push({
                category: expenseCategories[i],
                amount: parseFloat(expenseAmounts[i]),
                frequency: expenseFrequencies[i],
                essential: expenseEssential[i] === 'true'
            });
        }
    }
    
    // Collect debt data
    const debtTypes = formData.getAll('debt_type[]');
    const debtAmounts = formData.getAll('debt_amount[]');
    const debtInterests = formData.getAll('debt_interest[]');
    const debtMinimums = formData.getAll('debt_minimum[]');
    
    for (let i = 0; i < debtTypes.length; i++) {
        if (debtTypes[i] && debtAmounts[i] && debtInterests[i] && debtMinimums[i]) {
            financialProfile.debts.push({
                type: debtTypes[i],
                amount: parseFloat(debtAmounts[i]),
                interest_rate: parseFloat(debtInterests[i]),
                minimum_payment: parseFloat(debtMinimums[i])
            });
        }
    }
    
    // Show loading
    document.getElementById('financialForm').classList.add('hidden');
    document.getElementById('loading').classList.remove('hidden');
    
    try {
        // Send to API
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(financialProfile)
        });
        
        if (!response.ok) {
            throw new Error('Analysis failed');
        }
        
        const result = await response.json();
        
        // Display results
        document.getElementById('advice').textContent = result.financial_advice;
        document.getElementById('debt_ratio').textContent = result.debt_to_income_ratio;
        document.getElementById('risk_score').textContent = `${result.risk}/10`;
        document.getElementById('decrease_risk').textContent = result.decrease_risk;
        
        // Update risk indicator position
        const riskIndicator = document.getElementById('risk_indicator');
        const riskPosition = (result.risk / 10) * 100;
        riskIndicator.style.left = `${riskPosition}%`;
        
        // Update risk score color
        const riskScoreElement = document.getElementById('risk_score');
        if (result.risk <= 3) {
            riskScoreElement.style.color = '#059669'; // Green
        } else if (result.risk <= 6) {
            riskScoreElement.style.color = '#d97706'; // Orange
        } else {
            riskScoreElement.style.color = '#dc2626'; // Red
        }
        
        // Hide loading and show results
        document.getElementById('loading').classList.add('hidden');
        document.getElementById('results').classList.remove('hidden');
        
        // Scroll to results
        document.getElementById('results').scrollIntoView({ behavior: 'smooth' });
        
    } catch (error) {
        alert('Error analyzing profile: ' + error.message);
        document.getElementById('loading').classList.add('hidden');
        document.getElementById('financialForm').classList.remove('hidden');
    }
});