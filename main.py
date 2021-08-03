import block
from transactionList import *
from colorama import Fore, Style

init_block = block.TestBlock("first block", [t1, t2, t3])
print(init_block.data)
print("New hash: ", init_block.hash, "\n")


second_block = block.TestBlock(init_block.hash, [t4, t5, t6])
print(second_block.data)
print("New hash: ", second_block.hash, "\n")


third_block = block.TestBlock(second_block.hash, [t7, t8, t9])
print(third_block.data)
print("New hash: ", third_block.hash, "\n")


fourth_block = block.TestBlock(third_block.hash, [t10, t11, t12])
print(fourth_block.data)
print("New hash: ", fourth_block.hash, "\n")


last_hash = "c96a9973193b726f072b6f99bb307f5d603813920658f8a17e726f79b77d7b86"
if fourth_block.hash == last_hash:
    print(Fore.GREEN + "Success! All transactions are complete.")
else:
    print(Fore.RED + "Failure! We have any errors in transaction list.")
print(Style.RESET_ALL)
