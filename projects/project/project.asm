segment .data
	hello_str db "Hello, World!"


segment .bss


segment .text
	global main

jmp main

main:

push ebp
mov ebp, esp

	mov eax, 4
	mov ebx, 1
	mov ecx, hello_str
	mov edx, 32
	int 0x80

mov esp, ebp
pop ebp
ret

main_end:

