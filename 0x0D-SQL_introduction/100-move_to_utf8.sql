-- Changes DB encoding

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE
    first
    CONVERT TO CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_520_ci;

ALTER TABLE
    first_table
    CHANGE name name
    VARCHAR(256)
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_520_ci;
