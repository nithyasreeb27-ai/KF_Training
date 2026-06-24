logs = [
    ("2026-06-19 10:00", "INFO", "Model Loaded"),
    ("2026-06-19 10:05", "ERROR", "API Timeout"),
    ("2026-06-19 10:08", "WARNING", "High Memory"),
    ("2026-06-19 10:10", "INFO", "Prediction Completed"),
    ("2026-06-19 10:12", "ERROR", "API Timeout"),
    ("2026-06-19 10:15", "INFO", "Prediction Completed"),
    ("2026-06-19 10:18", "ERROR", "Database Connection Failed"),
    ("2026-06-19 10:20", "WARNING", "Disk Usage High"),
    ("2026-06-19 10:25", "INFO", "Model Reloaded"),
    ("2026-06-19 10:30", "ERROR", "API Timeout")
]

# Create a generator that yields one log record at a time.

def gen(logs):
    for log in logs:
        yield log
g=gen(logs)
for log in g:
    print(log)


# #Store all ERROR log messages in a new list.

# err_message=[]
# for i in logs:
#     if (i[1]=="ERROR"):
#         err_message.append(i[2])
# print(err_message)

# # Store all timestamps of WARNING logs.

# ts_warning=[]
# for i in logs:
#     if(i[1]=="WARNING"):
#         ts_warning.append(i[0])
# print(ts_warning)

# # Print each log using tuple unpacking.

# for i in logs:
#     time_stamp,log,message=i
#     print(i)

# # Create a tuple containing only (Timestamp, Message) for every ERROR log.

# # Pattern1
# for i in logs:
#     if i[1]=="ERROR":
#         time_stamp,log,message=i
#         t=(time_stamp,message)
#         print(t)

# # Pattern2

# lst=[]
# for i in logs:
#     if i[1]=="ERROR":
#         time_stamp,log,message=i
#         t=(time_stamp,message)
#         lst.append(t)
# print(lst)

# # Pattern3
# tpl=()
# for i in logs:
#     if i[1]=="ERROR":
#         time_stamp,log,message=i
#         tpl+=((time_stamp,message),)
# print(tpl)

# # Find all unique log levels.

# unique_log=[]
# for log in logs:
#     log_detail=log[1]
#     if log_detail not in unique_log:
#         unique_log.append(log_detail)
# print(unique_log)

# # Find unique error messages.

# unique_error=[]
# for log in logs:
#     if log[1]=="ERROR":
#         unique_error.append(log[2])
# print(set(unique_error))

# # Count the number of logs for each level.

# count_info=0
# count_error=0
# count_warning=0
# for log in logs:
#     if log[1]=="INFO":
#         count_info+=1
#     elif log[1]=="ERROR":
#         count_error+=1
#     elif log[1]=="WARNING":
#         count_warning+=1
# print("Count of info:",count_info)
# print("Count of error:",count_error)
# print("Count of warning:",count_warning)    

# # Count each error message.

# count_timeout=0
# count_db=0

# for time_stamp,level,message in logs:
#     if level=="ERROR":
#         if message=="API Timeout":
#             count_timeout+=1
#         elif message=="Database Connection Failed":
#             count_db+=1
# print("Count of timeout error:",count_timeout)
# print("Count of connection error:",count_db)

# # Extract all INFO messages.

# for timestamp,level,message in logs:
#     if level=="INFO":
#         print(message)

# # Extract all timestamps.
# for timestamp,level,message in logs:
#     print(timestamp)

# # Create a dictionary with log level as key and count as value.
# dict={}
# for timestamp,level,message in logs:
#     if level not in dict:
#         dict[level]=1
#     else:
#         dict[level]+=1
# print(dict)

# # Convert all log messages to uppercase.

# for timestamp,level,message in logs:
#     print(message.upper())

# # Extract only the date from each timestamp.

# for timestamp,level,message in logs:
#     ts=timestamp.split()
#     print(ts[0])

# # Filter only ERROR logs.

# er= list(filter(lambda x:x[1]=="ERROR",logs))
# print(er)


# er= filter(lambda x:x[1]=="ERROR",logs)
# print(er) # it is a iterator and can be used in for iterable and will be consumed after one iteration
# mp=list(map(lambda x:x[2],er))
# print(mp)

# er= list(map(lambda x:x[2],filter(lambda x:x[1]=="ERROR",logs)))
# print(er)

# # Filter logs whose message contains the word "Model".

# model=list(filter(lambda x:"Model" in x[2],logs))
# print(model)

# # get separately and then Combine them into a list of tuples.

# time_stamps=[]
# level=[]
# message=[]
# for i in logs:
#     time_stamps.append(i[0])
#     level.append(i[1])
#     message.append(i[2])
# lst=[]
# for num in range(len(time_stamps)):
#     tpl=(time_stamps[num],level[num],message[num])
#     lst.append(tpl)
# print(lst)

# # Create a dictionary mapping timestamp to message.

# # Pattern1
# time_stamps=[]
# level=[]
# message=[]
# for i in logs:
#     time_stamps.append(i[0])
#     level.append(i[1])
#     message.append(i[2])
# dict={}
# # Index
# for i in range(len(time_stamps)):
#     dict[time_stamps[i]]=message[i]
# print(dict)

# # Zip
# dict={}
# for ts,m in zip(time_stamps,message):
#     dict[ts]=m
# print(dict)


# # Pattern2
# dict={}
# for time_stamp,level,message in logs:
#     dict[time_stamp]=message
# print(dict)

# # Print log number before each log.

# for log in enumerate(logs,start=1):
#     print(f"{log[0]}.{log[1]}")

# # Create a dictionary where key is log number and value is the log tuple.

# dict={}
# for log in enumerate(logs,start=1):
#     dict[log[0]]=log[1]
# print(dict)

# # Create a generator that yields one ERROR log at a time.
# def gen(logs):
#     for log in logs:
#         if log[1]=="ERROR":
#             yield log
# g=gen(logs)
# print(next(gen(logs)))
# print(next(g))
# print(next(g))
# print(next(g))

# # Same 
# for log in g:
#     print(log)