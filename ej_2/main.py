import json
import pickle
# fix: change import path because in the pickle file search from a previosu folder
import sys

sys.path.append("/home/jaime/Desktop/test_python_developer_2")


from ej_2.enums.risk_enum import RiskEnum
from ej_2.services.ferretero import Ferretero
from ej_2.services.tuler import Tuler

input_data = json.load(
    open("/home/jaime/Desktop/test_python_developer_2/ej_2/data/input_data.json")
)

# not fix: in somewhere over the pickle file, exist a object using RiskEnum('ferretero'), but the RiskEnum('ferretero') is not a valid enum, which cause a ValueError
# i was here, i cant open the file ---> Exception has occurred. ValueError: 'ferretero' is not a valid RiskEnum
with open(
    "/home/jaime/Desktop/test_python_developer_2/ej_2/data/output_data.pickle", "rb"
) as file:
    expected_output = pickle.load(file)


def choose_model(input: dict):
    obj = None
    # fix: change RiskEnum('ferretero') to RiskEnum['ferretero'] because the first way is a invalid use of a enum
    if input["product_name"] == RiskEnum["ferretero"].value:
        obj = Ferretero(
            user_id=input["user_id"],
            product_name=input["product_name"],
            input_data=input["input_data"],
        )
    # fix: change RiskEnum('tuler') to RiskEnum['tuler'] because the first way is a invalid use of a enum
    elif input["product_name"] == RiskEnum["tuler"].value:
        obj = Tuler(
            user_id=input["user_id"],
            product_name=input["product_name"],
            input_data=input["input_data"],
        )
    return obj


def check_result(output_data):
    assert output_data == expected_output
    print("Buen trabajo")


def main():
    output_data = []
    for input in input_data:
        obj = choose_model(input)
        output_data.append(obj.risk_analysis())
    check_result(output_data)


if __name__ == "__main__":
    main()
