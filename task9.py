def my_custom_validation_function(
    one=True,
    two=True,
    three=True,
    four=True,
    five=True,
    six=False,
    seven=False,
    eight=False,
    nine=False,
    ten=False,
):
    if (
        one is True
        and two is True
        and three is True
        and four is True
        and five is True
        and six is False
        and seven is False
        and eight is False
        and nine is False
        and ten is False
    ):
        print("ok")


my_custom_validation_function(
    True, True, True, True, True, False, False, False, False, False
)
