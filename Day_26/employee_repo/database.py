import os
from supabase import create_client, Client
from dotenv import load_dotenv

# load environment variable from .env file
load_dotenv()

SUPABASE_URL = os.getenv("DAY_26_SUPABASE_URL")
SUPABASE_KEY = os.getenv("DAY_26_SUPABASE_KEY")
SUPABASE_BUCKET = os.getenv("DAY_26_SUPABASE_BUCKET")
SUPABASE_JWT_SECRET = os.getenv("DAY_26_SUPABASE_JWT_SECRET")

if not all([SUPABASE_URL, SUPABASE_KEY, SUPABASE_BUCKET]):
    raise ValueError("Missing environment variables")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# In supabase, we would be creating table using sql query
"""
create table employees (
  id serial primary key,
  first_name text not null,
  last_name text not null,
  email text unique not null,
  salary numeric not null,
  image_url text,
  is_active boolean default true
);
"""