from nada_dsl import *

def nada_main():

    partyA = Party(name="PartyA")
    partyB = Party(name="PartyB")

    secret_num1 = SecretInteger(Input(name="secret_num1", party=partyA))
    secret_num2 = SecretInteger(Input(name="secret_num2", party=partyA))
    secret_num3 = SecretInteger(Input(name="secret_num3", party=partyB))

    sum_result = secret_num1 + secret_num2
    final_result = sum_result * secret_num3

    return [Output(final_result, "final_output", partyA), Output(secret_num3, "secret_num3_output", partyB)]

