IDENTIFICATION DIVISION.
PROGRAM-ID. UninitializedVars.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-NUMBER1    PIC 9(5).
01 WS-NUMBER2    PIC 9(5).
01 WS-RESULT     PIC 9(5).

PROCEDURE DIVISION.
    ADD WS-NUMBER1 TO WS-NUMBER2 GIVING WS-RESULT.
   
    DISPLAY "Result: " WS-RESULT.

    STOP RUN.