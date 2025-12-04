-- additional tables needed for cyber cinic scan functionality

-- users table (using 'users' instead of 'user' to avoid SQL reserved word)
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- scan jobs table
CREATE TABLE IF NOT EXISTS scan_jobs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    target_id INTEGER NOT NULL,
    scan_type VARCHAR(50) NOT NULL,
    scan_config TEXT,
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    results TEXT,
    results_path VARCHAR(500),
    error_message TEXT
);

-- network targets table (simplified)
CREATE TABLE IF NOT EXISTS network_targets (
    id SERIAL PRIMARY KEY,
    target_name VARCHAR(100) NOT NULL,
    target_type VARCHAR(20) NOT NULL,
    target_value VARCHAR(255) NOT NULL,
    verified BOOLEAN DEFAULT FALSE,
    verification_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- insert default user for development
INSERT INTO users (username, email, password_hash, phone) 
VALUES ('dev_user', 'dev@cyberclinic.com', 'dev_password_hash', '555-0123')
ON CONFLICT (username) DO NOTHING;

-- insert default client for development  
INSERT INTO client (client_id, client_name, scan_frequency, last_scheduled)
VALUES ('dev-client-001', 'Development Client', 7, CURRENT_DATE)
ON CONFLICT (client_id) DO NOTHING;

-- create indexes for performance
CREATE INDEX IF NOT EXISTS idx_scan_jobs_status ON scan_jobs(status);
CREATE INDEX IF NOT EXISTS idx_scan_jobs_user_id ON scan_jobs(user_id);
CREATE INDEX IF NOT EXISTS idx_scan_jobs_created_at ON scan_jobs(created_at);
