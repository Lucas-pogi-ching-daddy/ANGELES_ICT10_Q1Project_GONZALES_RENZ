# NBA teams and their ticket prices
TEAMS = {
    "LAL": {"name": "Los Angeles Lakers", "price": 5000},
    "GSW": {"name": "Golden State Warriors", "price": 5500},
    "BOS": {"name": "Boston Celtics", "price": 5000},
    "NYK": {"name": "New York Knicks", "price": 4500},
    "CHI": {"name": "Chicago Bulls", "price": 4000},
    "MIA": {"name": "Miami Heat", "price": 4500},
    "DEN": {"name": "Denver Nuggets", "price": 5000},
    "MIL": {"name": "Milwaukee Bucks", "price": 4800},
}


# Gets an element from the webpage
def get_element(element_id):
    return document.querySelector(f"#{element_id}")


# Generates the NBA ticket SKU
def generate_sku(event):
    team = get_element("sku_team").value
    ticket_type = get_element("sku_type").value
    quantity = get_element("sku_qty").value

    if not quantity or int(quantity) < 1:
        get_element("sku_output").textContent = (
            "Please enter a valid ticket quantity."
        )
        return

    quantity = int(quantity)

    # Combines the category, team, ticket type, and quantity
    sku = f"NBA-{team}-{ticket_type}-{quantity:02d}"

    team_name = TEAMS[team]["name"]

    get_element("sku_output").innerHTML = (
        f"<strong>Generated SKU:</strong> {sku}<br>"
        f"<strong>Team:</strong> {team_name}<br>"
        f"<strong>Ticket Type:</strong> {ticket_type}<br>"
        f"<strong>Quantity:</strong> {quantity}"
    )


# Calculates the customer's NBA ticket order
def calculate_receipt(event):
    quantities = [
        int(get_element("qty1").value or 0),
        int(get_element("qty2").value or 0),
        int(get_element("qty3").value or 0),
        int(get_element("qty4").value or 0)
    ]

    teams = ["LAL", "GSW", "BOS", "NYK"]

    total = 0
    receipt = "<strong>NBA TICKET ORDER</strong><br><br>"

    for team, quantity in zip(teams, quantities):
        if quantity > 0:
            price = TEAMS[team]["price"]
            subtotal = price * quantity
            total += subtotal

            receipt += (
                f"{TEAMS[team]['name']} x {quantity} "
                f"= ₱{subtotal:,.2f}<br>"
            )

    if total == 0:
        receipt += "No tickets selected."
    else:
        receipt += (
            f"<br><strong>Total: ₱{total:,.2f}</strong>"
        )

    get_element("receipt_output").innerHTML = receipt