import re


class CPF_Validator:
    @classmethod
    def validate_cpf(cls, cpf):
        cpf_digits = re.findall(r"[0-9]", cpf)

        return (
            cls.__are_verifying_digits_valid(cpf_digits)
            and not cls.__are_all_digits_equal(cpf_digits)
        )

    @classmethod
    def __are_verifying_digits_valid(cls, cpf):
        return all(
            cls.__get_verifying_digit(vd_index, cpf) == int(cpf[vd_index])
            for vd_index in range(9, 11)
        )

    @staticmethod
    def __get_verifying_digit(vd_index, cpf):
        validation_sum = sum(
            (vd_index + 1 - index) * int(digit)
            for index, digit in enumerate(cpf[:(vd_index)])
        )

        validation_remainder = validation_sum % 11
        return 11 - validation_remainder if validation_remainder > 1 else 0

    @staticmethod
    def __are_all_digits_equal(cpf):
        return all(
            cpf[position] == cpf[position + 1]
            for position in range(len(cpf) - 1)
        )
