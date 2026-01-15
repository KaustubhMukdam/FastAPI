from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("DAY_26_SUPABASE_URL")
SUPABASE_KEY = os.getenv("DAY_26_SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# CRUD Operations
# Insert new row in table
# new_row = {'first_name' : 'Samarth'}
# supabase.table('demo-table').insert(new_row).execute()

# Update row in table
# updated_row = {'first_name' : 'Om'}
# supabase.table('demo-table').update(updated_row).eq('id', 1).execute()

# Delete row in table
# supabase.table('demo-table').delete().eq('id', 3).execute()

# results = supabase.table('demo-table').select('*').execute()    #To retrieve all records from table
# print(results)

# With the help of storage > bucket, we have created new bucket named 'demo-bucket' where we have stored an image
response = supabase.storage.from_('demo-bucket').get_public_url('max_image_5.jpg')
print(response)