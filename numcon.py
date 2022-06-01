import hashlib

print('--------------------------------')
print('Python Number Converter')
print('v1.0')
print('https://github.com/phosphor-1')
print('--------------------------------')

def main():
	conTarget = input ("Enter whole number to convert:")
	conTarget_int = int(conTarget)
	h = (hex (conTarget_int))
	b = (bin (conTarget_int))	
	md5 = hashlib.md5(conTarget.encode())
	sha1 = hashlib.sha1(conTarget.encode())
	sha256 = hashlib.sha256(conTarget.encode())
	sha512 = hashlib.sha512(conTarget.encode())	
	
	print('')
	print('Decimal: ' + (conTarget))
	print('')
	print('Hex: ' + (h[2:]))
	print('')
	print('Bin: ' + (b[2:]))
	print('')
	print('MD5: ' + (md5.hexdigest()))
	print('')
	print('SHA1: ' + (sha1.hexdigest()))
	print('')
	print('SHA256: ' + (sha256.hexdigest()))
	print('')
	print('SHA512: ' + (sha512.hexdigest()))
	print('')
	
while True:
    main()
    if input("Convert another number? (Y/N)").strip().upper() != 'Y':
        break


