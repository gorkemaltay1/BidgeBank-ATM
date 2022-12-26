from Personal.Card import Card
from Screen.Screen import Screen
from Personal.Account import Account
from Personal.Balance import Balance
from Transaction.Deposit import Deposit
from Transaction.Transfer import Transfer
from Transaction.Withdraw import Withdraw
from Transaction.Transaction import Transaction

print("YTÜ Matematik Mühendisliği Bankasına hoş geldiniz.") #Screen gözükecek.
counter = 3
while(counter > 0):
    kullanıcı_numarası = input("Lütfen Kart numarası giriniz:") 

    kullanıcı_şifresi = input("Lütfen Kart şifresi giriniz:")

    kullanıcı_Kartı = Card(kullanıcı_numarası,kullanıcı_şifresi)
    if(kullanıcı_Kartı.get_billing_address()):
        hesap_numarası = kullanıcı_Kartı.get_customer_account_number()
        menuScreen = Screen()
        customerDatas = Account(hesap_numarası).AccountAmount()
        totalBalance = customerDatas[0]
        availableBalance = customerDatas[1]
        accountType = customerDatas[2]
        Screen.show_message(menuScreen,f"{kullanıcı_Kartı.get_customer_name()} hoş geldin.")
        menuOptions = "Deposit      Withdraw        Transfer        Balance Inquiry     Internal Transfer   Exit/Take Card"
        Screen.show_message(menuScreen,message=menuOptions)
        choice = input("Lüften bir seçim yapınız:")
        # Withdraw bitti.
        if choice == 'Withdraw':
            withdrawOptions = "$20      $40     $100    Customer amount     Cancel"
            Screen.show_message(menuScreen,withdrawOptions)
            withdrawChoice = input("Seçeneklerden birini seçiniz:")
            if withdrawChoice == "$20" and availableBalance>20:
                print("$20 veriliyor...")
                availableBalance = availableBalance - 20
                totalBalance = totalBalance - 20
                Withdraw(hesap_numarası).accountBalanceWithdraw(20)
                Transaction("Completed").make_transaction(choice,hesap_numarası)
            elif withdrawChoice == "$40" and availableBalance>40:
                print("$40 veriliyor...")
                Withdraw(hesap_numarası).accountBalanceWithdraw(40)
                Transaction("Completed").make_transaction("Withdraw",hesap_numarası)
            elif withdrawChoice == "$100" and availableBalance>100:
                print("$100 veriliyor...")
                availableBalance = availableBalance - 100
                totalBalance = totalBalance - 100
                Withdraw(hesap_numarası).accountBalanceWithdraw(100)
                Transaction("Completed").make_transaction("Withdraw",hesap_numarası)
            elif withdrawChoice == "Customer amount":
                desiredWithdraw = int(input("Çekmek istediğiniz para miktarını giriniz"))
                if desiredWithdraw>availableBalance:
                    print("Bu işlem için yeteri kadar paranız yok.")
                    Transaction("Not Completed").make_transaction("Withdraw",hesap_numarası)
                else:
                    print(f"${desiredWithdraw} veriliyor.")
                    Withdraw(hesap_numarası).accountBalanceWithdraw(desiredWithdraw)
                    Transaction("Completed").make_transaction("Withdraw",hesap_numarası)
        #Deposit bitti.
        elif choice == "Deposit":
            amount = input("Please enter amount")
            print(f"{amount} the amount you entered")
            controlAmount = input("Is this correct")
            if controlAmount == "Yes":
                choiceAccount = input("Do you want to checking or saving?")
                if choiceAccount == "checking":
                    print("Your money add checking account")
                    Deposit(hesap_numarası).deposit_transaction(amount)
                    Transaction("Completed").make_transaction("Deposit",hesap_numarası)
                elif choiceAccount == "saving":
                    print("Your money add saving account")
                    Deposit(hesap_numarası).deposit_transaction(amount)
                    Transaction("Completed").make_transaction("Deposit",hesap_numarası)
                else:
                    print("Your money don't add your account")
                    Transaction("Not Completed").make_transaction("Deposit",hesap_numarası)
                    counter = 0
            elif controlAmount == "No":
                print("You don't correct amount")
                choiceAccount = input("Do you want to checking or saving?")
                if choiceAccount == "checking":
                    print("Your money add checking account")
                    # checking hesabını güncelle
                elif choiceAccount == "saving":
                    print("Your money add saving account")
                    # saving hesabını güncelle.
                    # Bu modül manasız
                else:
                    print("Your money don't add your account")
                    counter = 0
            counter = 0
        # Transfer bitti.
        elif choice == "Transfer":
            control = 3
            while control > 0: 
                transferAmount = int(input("Please enter the amount you want to transfer:"))
                if transferAmount <= availableBalance:
                    accountReceivedNumber = int(input("Please enter account number"))
                    if Transfer(accountReceivedNumber,hesap_numarası).destination_number_check():
                        Transfer(accountReceivedNumber,hesap_numarası).transferring_money(transferAmount)
                        Transaction("Completed").make_transaction("Transfer",hesap_numarası)
                        print("accounts updated")
                    else:
                        print("There is no client with this account number.")
                        retryTransaction = input("Do you want to retry transaction")
                        if retryTransaction:
                            control -= 1
                        else:
                            control = 0
                            counter = 0 
                    receipt = input("Do you want to print receipt")
                    if receipt:
                        print("print receipt")
                    counter = 0
                    control = 0
                else:
                    print("You don't have enough money")
                    retryTransaction = input("Do you want to retry transaction")
                    if retryTransaction:
                        control -= 1
                    else:
                        control = 0
                        counter = 0 
        # Balance bitti.
        elif choice == "Balance Inquiry":
            result = Balance(hesap_numarası).accountBalance(hesap_numarası)
            print(result[0][1],result[0][2])    
        # Internal bitti.
        elif choice == "Internal Transfer":
            # Paraya çekeceğin hesabı seçiniz:
            account_choice = int(input("Hesap numarası gitiniz"))
            transfer_money = int(input("Ne kadar para transfer etmek isteriniz:"))
            if availableBalance > transfer_money:
                Transfer(account_choice,hesap_numarası).transferring_money(transfer_money)
            else:
                # Front ekibi bu kısmı Error hatası şeklinde kırmızı versin.
                print("İşleminiz gerçekleştirilmedi")
        # Exit/Take Card bitti.
        elif choice == "Exit/Take Card":
            counter = 0
    else:
        counter = counter - 1
        if counter == 0:
            print("Hakkınız kalmadı.")
        else:
            print(f"{counter} hakkınız kaldı.")
    
print("Hoşca kalın...")



