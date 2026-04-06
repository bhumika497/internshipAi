from datetime import datetime, timedelta
import random

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.created_at = datetime.now()


class Plan:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Subscription:
    def __init__(self, user_id, plan_id):
        self.user_id = user_id
        self.plan_id = plan_id
        self.start_date = datetime.now()
        self.next_billing_date = datetime.now() + timedelta(days=30)
        self.status = "Active"


class Invoice:
    def __init__(self, id, user_id, amount):
        self.id = id
        self.user_id = user_id
        self.amount = max(0, amount)
        self.status = "Pending"
        self.coupon_applied = None
        self.discount_amount = 0
        self.created_at = datetime.now()


class Payment:
    def __init__(self, invoice_id, amount):
        self.invoice_id = invoice_id
        self.amount = amount
        self.status = "Pending"
        self.retry_count = 0


class SubscriptionSystem:

    def __init__(self):
        self.users = []
        self.subscriptions = []
        self.invoices = []
        self.user_id = 1
        self.invoice_id = 1

        self.plans = [
            Plan(1, "Free", 0),
            Plan(2, "Pro", 10),
            Plan(3, "Enterprise", 30)
        ]

    def create_user(self):
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        user = User(self.user_id, name, email)
        self.users.append(user)
        self.user_id += 1
        print("User Created Successfully!")
        return user

    def view_users(self):
        for user in self.users:
            print(user.id, user.name, user.email)

    def show_plans(self):
        print("\nAvailable Plans:")
        for plan in self.plans:
            print(f"{plan.id}. {plan.name} - ${plan.price}")

    def subscribe(self, user):
        self.show_plans()
        choice = int(input("Select Plan: "))
        plan = next((p for p in self.plans if p.id == choice), None)

        if not plan:
            print("Invalid Plan")
            return

        subscription = Subscription(user.id, plan.id)
        self.subscriptions.append(subscription)

        print(f"{user.name} subscribed to {plan.name}")

        if plan.price > 0:
            self.create_invoice(user.id, plan.price)

    def create_invoice(self, user_id, amount):
        invoice = Invoice(self.invoice_id, user_id, amount)
        self.invoice_id += 1

        self.apply_coupon(invoice)
        self.invoices.append(invoice)
        self.process_payment(invoice)

    def apply_coupon(self, invoice):
        print("\nAvailable Coupons:")
        
        coupons = [
            {"code": "WELCOME10", "type": "percentage", "value": 10},
            {"code": "FESTIVE20", "type": "percentage", "value": 20},
            {"code": "FLAT10", "type": "flat", "value": 10}
        ]

        for idx, c in enumerate(coupons, 1):
            print(f"{idx}. {c['code']} - {c['type']} {c['value']}")

        choice = int(input("Select Coupon (0 for none): "))

        if choice == 0:
            return

        coupon = coupons[choice - 1]

        if coupon["type"] == "percentage":
            discount = invoice.amount * coupon["value"] / 100
        else:
            discount = coupon["value"]

        invoice.amount = max(0, invoice.amount - discount)
        invoice.discount_amount = discount
        invoice.coupon_applied = coupon["code"]

        print(f"Coupon Applied: {coupon['code']} | Discount: {round(discount,2)}")

    def process_payment(self, invoice):
        payment = Payment(invoice.id, invoice.amount)

        success = random.choice([True, False])

        if success:
            payment.status = "Success"
            invoice.status = "Paid"
            print("Payment Successful")
        else:
            payment.status = "Failed"
            invoice.status = "Failed"
            payment.retry_count += 1
            print("Payment Failed")
            self.retry_payment(payment, invoice)

    def retry_payment(self, payment, invoice):
        while payment.retry_count < 3:
            print("Retrying Payment...")
            success = random.choice([True, False])

            if success:
                payment.status = "Success"
                invoice.status = "Paid"
                print("Payment Successful")
                return

            payment.retry_count += 1

        invoice.status = "Overdue"

        sub = next((s for s in self.subscriptions if s.user_id == invoice.user_id), None)
        if sub:
            sub.status = "Overdue"

        print("Payment Overdue - Subscription marked as Overdue")

    def upgrade_plan(self):
        if not self.subscriptions:
            print("No subscriptions found")
            return

        self.view_users()
        user_id = int(input("Enter User ID: "))

        subscription = next((s for s in self.subscriptions if s.user_id == user_id), None)

        if not subscription:
            print("Subscription not found")
            return

        self.show_plans()
        new_plan_id = int(input("Enter New Plan ID: "))
        new_plan = next((p for p in self.plans if p.id == new_plan_id), None)

        if not new_plan:
            print("Invalid Plan")
            return

        current_plan = next((p for p in self.plans if p.id == subscription.plan_id), None)

        if current_plan.id == new_plan.id:
            print("Already on this plan")
            return

        remaining_days = (subscription.next_billing_date - datetime.now()).days
        total_days = 30

        prorated_amount = max(0, (remaining_days / total_days) * new_plan.price)

        subscription.plan_id = new_plan.id

        print(f"Plan changed to {new_plan.name}")
        print(f"Prorated Amount: {round(prorated_amount,2)}")

        if prorated_amount > 0:
            self.create_invoice(user_id, prorated_amount)

    def run_billing_cycle(self):
        print("\n--- Running Billing Cycle ---")

        for sub in self.subscriptions:
            if sub.status != "Active":
                continue

            if datetime.now() >= sub.next_billing_date:
                plan = next((p for p in self.plans if p.id == sub.plan_id), None)

                if plan.price > 0:
                    self.create_invoice(sub.user_id, plan.price)

                sub.next_billing_date += timedelta(days=30)

    def cancel_subscription(self):
        if not self.subscriptions:
            print("No subscriptions to cancel")
            return

        self.view_users()
        user_id = int(input("Enter User ID: "))

        subscription = next((s for s in self.subscriptions if s.user_id == user_id), None)

        if subscription:
            subscription.status = "Canceled"
            print("Subscription canceled")
        else:
            print("Subscription not found")


def main():
    system = SubscriptionSystem()

    while True:
        print("\n===== Subscription Billing System =====")
        print("1. Create User")
        print("2. Subscribe Plan")
        print("3. Upgrade/Downgrade Plan")
        print("4. Cancel Subscription")
        print("5. View Users")
        print("6. Run Billing Cycle")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.create_user()

        elif choice == "2":
            if not system.users:
                print("Create user first")
                continue

            system.view_users()
            user_id = int(input("Select User ID: "))
            user = next((u for u in system.users if u.id == user_id), None)

            if user:
                system.subscribe(user)

        elif choice == "3":
            system.upgrade_plan()

        elif choice == "4":
            system.cancel_subscription()

        elif choice == "5":
            system.view_users()

        elif choice == "6":
            system.run_billing_cycle()

        elif choice == "7":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()