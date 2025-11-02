from pyscript import document

def order_food(e):
    order_summary = document.getElementById("summary-content")
    order_summary.innerHTML = ""

    name = document.getElementById("name").value.strip()
    number = document.getElementById("phone").value.strip()
    address = document.getElementById("address").value.strip()

    checkboxes = document.querySelectorAll("form input[type='checkbox']")
    subtotal = 0.0
    items = []

    for checkbox in checkboxes:
        if checkbox.checked:
            price = float(checkbox.getAttribute("data-price"))
            subtotal += price
            items.append(checkbox.nextElementSibling.innerText)  

    items_list = "\n    ".join(items)
    summary_message = f"""Order for:  {name}
    Address:    {address}
    Number:     {number}

    Items Ordered:
    {items_list}

    Subtotal: {subtotal:.2f}
    """

    order_summary.innerText = summary_message


    if not name or not address or not number:
        order_summary.innerHTML = "'Please fill up all forms before finalizing your order.'"
        return
    if not items:
        order_summary.innerHTML = "'Please select at least one of the items.'"
        return