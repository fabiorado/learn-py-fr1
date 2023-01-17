CREATE TABLE IF NOT EXISTS user (
	UserID              varchar(50) NULL,
	FullName            text NULL,
    PreferredName       varchar(255) NULL,
    LogonName           varchar(255) NULL,
    HashedPassword      text NULL,
	EmailAddress        varchar(255) NULL,
	PhoneNumber         varchar(50) NULL,
    CustomFields        text NULL, -- JSON with the content of the "Other" fields
    UserPreferences     text NULL, -- JSON with interface preferences
	IsPermittedToLogon  boolean NOT NULL DEFAULT 1,
    IsUserAdmin         boolean NOT NULL DEFAULT 0,

    -- Control
	CreatedByID         varchar(50) NULL,
	CreatedOn           timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	ModifiedByID        varchar(50) NULL,
	ModifiedOn          timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- SCD2 
    IsCurrent           boolean NOT NULL DEFAULT 1,
    IsDeleted           boolean NOT NULL DEFAULT 0,
    ValidFrom           timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ValidTo             timestamp NOT NULL DEFAULT '9999-12-31 00:00:00'
);