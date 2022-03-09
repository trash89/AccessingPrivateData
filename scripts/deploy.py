from brownie import accounts, network, config, Vault, StorageTest
from brownie import web3


def main():
    st = StorageTest.deploy({"from": accounts[0]})
    print(f"StorageTest deployed at {st}")
    print(web3.toHex(web3.eth.getStorageAt(st.address, 0)))
    print(web3.toInt(hexstr=web3.toHex(
        web3.eth.getStorageAt(st.address, 0))[-2:]))
    print(web3.toInt(hexstr=web3.toHex(
        web3.eth.getStorageAt(st.address, 0))[-4:-2]))
    print(web3.toHex(web3.eth.getStorageAt(st.address, 0))[-46:-6])
    print(web3.toHex(web3.eth.getStorageAt(st.address, 0))[-48:-46])
    print(web3.toInt(hexstr=web3.toHex(
        web3.eth.getStorageAt(st.address, 0))[-50:-48]))

    pwd = web3.toHex(text="secret")
    v = Vault.deploy(pwd, {"from": accounts[0]})
    print(f"Vault deployed at {v}")

    print(web3.toInt(web3.eth.getStorageAt(v.address, 0)))
    print(web3.toHex(web3.eth.getStorageAt(v.address, 1)))

    txt = web3.eth.getStorageAt(v.address, 1)
    s16 = slice(16)
    print(s16)
    print(web3.toInt(txt[s16]))
    s17 = slice(16, 17)
    print(web3.toInt(txt[s17]))

    print(web3.eth.getStorageAt(v.address, 2).decode("utf-8"))

    pwdu0 = web3.toHex(text="pwduser0")
    pwdu1 = web3.toHex(text="pwduser1")
    pwdu2 = web3.toHex(text="pwduser2")

    print("Creating two users...")
    tx = v.addUser(pwdu0, {"from": accounts[0]})
    tx.wait(1)
    tx = v.addUser(pwdu1, {"from": accounts[0]})
    tx.wait(1)
    tx = v.addUser(pwdu2, {"from": accounts[0]})
    tx.wait(1)

    print(
        f"Array length after adding 3 users : {web3.toInt(web3.eth.getStorageAt(v.address, 6))}")
    array_loc = v.getArrayLocation(6, 0, 2)
    print(f"Array location starts at : {array_loc}")

    print(web3.toInt(web3.eth.getStorageAt(v.address, web3.toHex(array_loc))))
    print(web3.eth.getStorageAt(v.address, web3.toHex(array_loc+1)).decode("utf-8"))

    print(web3.toInt(web3.eth.getStorageAt(v.address, web3.toHex(array_loc+2))))
    print(web3.eth.getStorageAt(v.address, web3.toHex(array_loc+3)).decode("utf-8"))

    print(web3.toInt(web3.eth.getStorageAt(v.address, web3.toHex(array_loc+4))))
    print(web3.eth.getStorageAt(v.address, web3.toHex(array_loc+5)).decode("utf-8"))

    print("Getting from map[key=1]")
    map_loc = v.getMapLocation(7, 1)
    print(f"Map location starts at : {map_loc}")
    print(web3.toInt(web3.eth.getStorageAt(v.address, web3.toHex(map_loc))))
    print(web3.eth.getStorageAt(v.address, web3.toHex(map_loc+1)).decode("utf-8"))

    print("Getting from map[key=2]")
    map_loc = v.getMapLocation(7, 2)
    print(f"Map location starts at : {map_loc}")
    print(web3.toInt(web3.eth.getStorageAt(v.address, web3.toHex(map_loc))))
    print(web3.eth.getStorageAt(v.address, web3.toHex(map_loc+1)).decode("utf-8"))
