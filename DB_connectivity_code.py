import psycopg2

dbname = "nexa-crm-ai-dev"
user = "avnadmin"
password = "Digital!23"
host = "nagarjuna-crm-dbs.postgres.database.azure.com"  # defaults to localhost if not provided
port = "5432"  # defaults to 5432 if not provided

# Connect to the database
conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
cur = conn.cursor()

print('connection created')

#create new column in nexa-crm-ai-dev table in leads #course #fee_quoted_string #call_recorded_file_name
#alter_table_query = 'ALTER TABLE public.leads ADD COLUMN course VARCHAR(100), ADD COLUMN fee_quoted_string VARCHAR(255), ADD COLUMN call_recorded_file_name VARCHAR(100);'
#delete_query = f"ALTER TABLE public.leads DROP COLUMN call_recorded_file_name;"
#max_calls_id = 'select max("callsId") from public.leads'                               #batchTiming                                                        #course         #nextFollowUp
insert_query = 'insert into public.leads (name, "countryCode", phone, email, "feeQuoted", "batchTiming", description, "leadStatus", "leadSource", "techStack", "classMode", "nextFollowUp", "createdAt", "updatedAt") values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW())'

name_string = f'Saarath'
country_code = f'+{91}'
phone = 9381629945
email_string = f'saarath@gmail.com'
fee_quoted_string = f'50000 for cloud computing with internship'
batch_timing_string = '{8AM - 10AM}'                        #########################################################
description_string = f'I am interested in learning new technologies like ai, ml, dl, tl, nlp, cv'
lead_status_string = f'Warm Lead'
lead_source_string = f'Student Referral'
tech_stack_string = f'Design'
course_string = '[4]'
class_mode_string = f'HYD ClassRoom'
next_follow_up_timestamp = '06-03-2024' #mm-dd-yy      #time-stamp  ##################################################
calls_id = 1111



insert_values = (name_string, country_code, phone, email_string, fee_quoted_string, batch_timing_string, description_string, lead_status_string, lead_source_string, tech_stack_string, class_mode_string, next_follow_up_timestamp)
#fetch_file_name = f"select id, filename from public.calls where id = 1"

cur.execute(insert_query, insert_values)
#cur.execute(query)
#print(cur.fetchall())

# Commit the changes
conn.commit()

# fetch_query = f"select filename from public.calls where id = {ids}"
# cur.execute(fetch_query)
# result2 = cur.fetchone()

# Close the cursor and connection
cur.close()
conn.close()
print("connection closed")