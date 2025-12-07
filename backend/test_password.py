from werkzeug.security import check_password_hash

# Test the password hash from your database
test_hash = "scrypt:32768:8:1$xkKbH6i74TGGgNOf$7861fe2f50964c6e5bcb39f87e3fa00701c9408a4ade1b9ba01c4584210f7f555fc3a791489419ede6d35924b4b28fec2294cf0af28764426d172fed48e4df40"
test_password = "test123"  # This is from your database dump

result = check_password_hash(test_hash, test_password)
print(f"Password check result: {result}")