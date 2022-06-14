#where cell values are placed
cellmapping = {
 "EMAIL ADDRESS": "D1",
 "MONTHLY INCOME": "A4",
 "MONTHLY EXPENSES": "C4",
 "CASHFLOW": "e4",
 "PRO FORMA CAP RATE": "G4",
 "PURCHASE PRICE": "C9",
 "NOI": "B7",
 "TOTAL CASH NEEDED": "C7",
 "ROI": "e7",
 "PURCHASE CAP RATE": "g7",
 "CLOSING COSTS": "C10",
 "REPAIRS": "C11",
 "ADDRESS": "B15",
 "DOWN PAYMENT": "C19",
 "AMORTIZED OVER": "C22",
 "LOAN INTEREST RATE": "C23",
 "MONTHLY P&I": "C24",
 "EMAIL ADDRESS": "B1",
 "UTILITIES": "c27",
 "INSURANCE": "c30",
 "HOA FEES": "c32",
 "PROPERTY DESCRIPTION": "A17",
 "RENTAL PROPERTY IMAGE?": "f17",
}

#CELLNAMES
nameMapping = {
 "Email Address": "a1",
 "Monthly Income": "A3",
 "Monthly Expenses": "C3",
 "CashFlow": "E3",
 "Pro Forma Cap Rate": "G3",
 "NOI": "A6",
 "Total Cash Needed": "C6",
 "ROI": "E6",
 "Puchase Cap Rate": "G6",
 "Purchase Price": "A9",
 "Closing Costs": "A10",
 "Repairs": "A11",
 "Total Value of Investment": "a12",
 "Address": "a15",
 "Property Description": "a16",
 "Property Image": "f14",
 "Down Payment": "a19",
 "Loan Amount": "a20",
 "Loan Points": "a21",
 "Amortized Over": "a22",
 "Loan Interest Rate": "a23",
 "Monthly P&I": "a24",
 "50% Rule Cash Flow Estimates": "e19",
 "Total Monthly Income": "e20",
 "Total Monthly Cash Flow using 50% Rule": "e21",
 "Monthly Payment/Interest Payment": "e22",
 "50% Rule Cash Flow": "e24",
 "Expenses": "a26",
 "Utilities": "a27",
 "Vacancy": "a28",
 "Cap Ex": "a29",
 "Insurance": "a30",
 "Mortgage Payment": "a31",
 "HOA Fees": "a32",
 "Maintenance": "a33",
 "Management": "a34",
 "Property Taxes": "a35",
 "Debt Coverage Ratio": "a38",
 "Total Expenses": "a36",
}


#RPQSHEET LETTERS(Column Letters)
letters = {
 'b': "EMAIL ADDRESS",
 'c': "ADDRESS",
 'd': "PROPERTY DESCRIPTION",
 'e': "PURCHASE PRICE",
 'f': "CLOSING COSTS",
 'g': "REPAIRS",
 'h': "DOWN PAYMENT",
 'i': "LOAN INTEREST RATE",
 'j': "MONTHLY P&I",
 'k': "MONTHLY INCOME",
 "l": "AMORTIZED OVER",
 'm': "MONTHLY EXPENSES",
 'n': "INSURANCE",
 'o': "UTILITIES",
 'P': 'HOA FEES',
 'q': "RENTAL PROPERTY IMAGE?"
 }
 
#COLORLAYOUT FOR SPREADSHEET
colorMapping = {
 "a3": "black",
 "b3": "black",
 "c3": "black",
 "d3": "black",
 "e3": "black",
 "f3": "black",
 "g3": "black",
 "h3": "black",

 
 "a4": "#E1E3E6",
 "b4": "#E1E3E6",
 "c4": "#E1E3E6",
 "d4": "#E1E3E6",
 "e4": "#E1E3E6",
 "f4": "#E1E3E6",
 "g4": "#E1E3E6",
 "h4": "#E1E3E6",
 
 "a5": "#4285f4", 
 "b5": "#4285f4",
 "c5": "#4285f4",
 "d5": "#4285f4",
 "d5": "#4285f4",
 "e5": "#4285f4",
 "f5": "#4285f4",
 "g5": "#4285f4",
 "h5": "#4285f4",
 
 
 "a6": "black",
 "b6": "black",
 "c6": "black",
 "d6": "black",
 "e6": "black",
 "f6": "black",
 "g6": "black",
 "h6": "black",
 
 "a7": "#E1E3E6", 
 "b7": "#E1E3E6",
 "c7": "#E1E3E6",
 "d7": "#E1E3E6",
 "e7": "#E1E3E6",
 "f7": "#E1E3E6",
 "g7": "#E1E3E6",
 "h7": "#E1E3E6",
}

borderPlacement = {}

textclr = {
 "a3": "white",
 "c3": "white",
 "e3": "white",
 "g3": "white",
 
 "a6": "white",
 "c6": "white",
 "e6": "white",
 "g6": "white",
}

functionMapping = {
 "TOTAL VALUE OF INVESTMENT": {
   "cell": "c12",
   "eqfunc": "=SUM(c9:c11)",
 }, 

 "TOTAL EXPENSES": {
   "cell": "c36",
   "eqfunc": "=SUM(c27:c35)",
 },
 "PROPERTY TAXES": {
   "cell": "c35",
   "eqfunc": "=C9*2.97%/12",
 },
 "DEBT COVERAGE RATIO": {
   "cell": "c38",
   "eqfunc": "=c24/a7*100",
 },
 "VACANCY": {
   "cell": "c28",
   "eqfunc": "=a4*12*5%/12"
 },
 "CAP EX": {
   "cell": "c29",
   "eqfunc": "=a4*12*10%/12",
 },
 "MAINTENANCE" : {
   "cell": "c33",
   "eqfunc": "=a4*12*5%/12",
 },
 "MANAGEMENT" : {
   "cell": "c34",
   "eqfunc": "=a4*12*10%/12",
 },
}
