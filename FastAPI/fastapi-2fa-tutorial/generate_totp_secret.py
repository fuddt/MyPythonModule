import pyotp

# 新しいTOTPシークレットキーを生成
secret = pyotp.random_base32()
print("TOTP Secret:", secret)