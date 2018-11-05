import threading
import bitlib


def run(name):
    print("{} started!".format(name))

    while True:
        private_key = bitlib.BitGen.generate_private_key()
        wif = bitlib.BitGen.private2wif(private_key)
        address = bitlib.BitGen.private2address(private_key)
        balance = bitnet.get_balance(address)

        message = "private:{},wif:{},address:{},balance:{}\n".format(
            private_key, wif, address, balance)

        if bitconf.log:
            print(message)

        if balance.isdigit() == False:
            print(balance)
            continue

        if balance != "0":
            f = open("success.txt", "a")
            f.write(message)
            f.close()
            print(message)
            bitmail.send_email(message)


if __name__ == '__main__':
    bitconf = bitlib.BitConf()
    bitconf.load()
    bitmail = bitlib.BitMail(bitconf.smtp_host, bitconf.smtp_port,
                             bitconf.smtp_username, bitconf.smtp_password)
    bitnet = bitlib.BitNet(bitconf.http_proxy_url, bitconf.http_proxy_port)

    bitmail.send_email("I am runing")
    for x in range(bitconf.thread_count):
        thread_name = "Thread-{}".format(x + 1)
        mythread = threading.Thread(target=run, args=(thread_name,))
        mythread.start()
