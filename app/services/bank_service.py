import abc

from app.services.account_service import AccountService


class BankService(abc.ABC):

    def deposit_money_at_atm(self, account_id: int, amount: int) -> None:
        """
        Deposit money at the ATM
        """
        ...

    def deposit_money_at_branch(self, account_id: int, amount: int) -> None:
        """
        Deposit money at the bank branch
        """
        ...

    def make_transfer_at_atm(self, from_account_id: int, to_account_id: int, amount: int) -> None:
        """
        Make a transfer at the ATM
        """
        ...

    def make_transfer_at_branch(self, from_account_id: int, to_account_id: int, amount: int) -> None:
        """
        Make a transfer at the bank branch
        """
        ...

    def withdraw_money_at_atm(self, account_id: int, amount: int) -> None:
        """
        Withdraw money at the ATM
        """
        ...

    def withdraw_money_at_branch(self, account_id: int, amount: int) -> None:
        """
        Withdraw money at the bank branch
        """
        ...

class BranchBankService(BankService):
    def __init__(self, account_service: AccountService):
        self.account_service = account_service

    def deposit_money_at_atm(self, account_id: int, amount: int) -> None:
        """
        Deposit money at the ATM
        """
        raise NotImplementedError("ATM deposits are not supported by BranchBankService.")

    def deposit_money_at_branch(self, account_id: int, amount: int) -> None:
        """
        Deposit money at the bank branch
        """
        self.account_service.deposit_money(account_id, amount)

    def make_transfer_at_atm(self, from_account_id: int, to_account_id: int, amount: int) -> None:
        """
        Make a transfer at the ATM
        """
        raise NotImplementedError("ATM transfers are not supported by BranchBankService.")

    def make_transfer_at_branch(self, from_account_id: int, to_account_id: int, amount: int) -> None:
        """
        Make a transfer at the bank branch
        """
        self.account_service.transfer_money(from_account_id, to_account_id, amount)

    def withdraw_money_at_atm(self, account_id: int, amount: int) -> None:
        """
        Withdraw money at the ATM
        """
        raise NotImplementedError("ATM withdrawals are not supported by BranchBankService.")

    def withdraw_money_at_branch(self, account_id: int, amount: int) -> None:
        """
        Withdraw money at the bank branch
        """
        self.account_service.withdraw_money(account_id, amount)

