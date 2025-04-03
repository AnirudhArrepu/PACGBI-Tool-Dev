IDENTIFICATION DIVISION.
PROGRAM-ID. BankLoopError.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 COUNTER     PIC 9(2) VALUE ZEROS.
01 LIMIT       PIC 9(2) VALUE 10.
01 TOTAL       PIC 9(5) VALUE ZEROS.

PROCEDURE DIVISION.
    PERFORM UNTIL COUNTER > LIMIT
        ADD 1 TO COUNTER
        ADD COUNTER TO TOTAL
        DISPLAY "Current Total: " TOTAL
    END-PERFORM.
   
    DISPLAY "Final Total: " TOTAL.

    STOP RUN.