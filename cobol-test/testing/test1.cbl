IDENTIFICATION DIVISION.
PROGRAM-ID. BankOverflow.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 TOTAL-AMOUNT     PIC 9(5) VALUE ZEROS.
01 TRANSACTION-AMT  PIC 9(5).

PROCEDURE DIVISION.
    DISPLAY "Enter transaction amount: " WITH NO ADVANCING.
    ACCEPT TRANSACTION-AMT.
    
    ADD TRANSACTION-AMT TO TOTAL-AMOUNT.
    
    IF TOTAL-AMOUNT > 99999
        DISPLAY "ERROR: Overflow occurred in total amount calculation."
    ELSE
        DISPLAY "Updated Total Amount: " TOTAL-AMOUNT.
    END-IF.

    STOP RUN.
