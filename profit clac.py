# Profit and Loss Calculator with Percentage

# Get input from the user
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

# Calculate profit or loss
if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percent = (profit / cost_price) * 100
    print(f"Profit: {profit:.2f}")
    print(f"Profit Percentage: {profit_percent:.2f}%")
elif cost_price > selling_price:
    loss = cost_price - selling_price
    loss_percent = (loss / cost_price) * 100
    print(f"Loss: {loss:.2f}")
    print(f"Loss Percentage: {loss_percent:.2f}%")
else:
    print("No profit, no loss.")

# Keep the window open
input("\nPress Enter to exit...")
