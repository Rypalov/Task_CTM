# list_block = [[192, 168, 0, 2], [192, 168, 1, 3], [100, 168, 1, 254], [192, 168, 0, 6]]
# # list_block = [[191, 168, 1, 3], [194, 168, 1, 3]]
# # list_block = [[192, 168, 1, 2], [192, 168, 1, 3], [192, 168, 1, 5]]
#
# def ip_to_int(a, b, c, d):
#     return (a << 24) + (b << 16) + (c << 8) + d
#
# def maske(ip1, ip2):
#     m = 0xFFFFFFFF ^ ip_to_int(*ip1) ^ ip_to_int(*ip2)
#     block_one = (m & (0xFF << 24)) >> 24
#     if block_one == 255:
#         block_two = (m & (0xFF << 16)) >> 16
#         if block_two == 255:
#             block_three = (m & (0xFF << 8)) >> 8
#             if block_three == 255:
#                 block_four = (m & (0xFF << 0)) >> 0
#             else:
#                 block_four = 0
#         else:
#             block_three = 0
#             block_four = 0
#     else:
#         block_two = 0
#         block_three = 0
#         block_four = 0
#     return block_one, block_two, block_three, block_four
#
#
# def sub_net(ip_list: list, mask: list):
#     block: list = ["", "", "", ""]
#     for i in range(1, 4):
#         if mask[i] == 255:
#             block[i] = ip_list[0][i]
#         else:
#             block[i] = 0
#     if mask[0] == 0:
#         block[0] = mask[0]
#     elif mask[0] == 255:
#         block[0] = ip_list[0][0]
#     elif mask[0] < 128:
#         block[0] = 0
#     else:
#         block[00] = mask[0] // 8 * 8
#     return f"{block[0]}.{block[1]}.{block[2]}.{block[3]}"
#
#
# def get_prefix(mask: list):
#     prefix: int = 0
#     for x in mask:
#         x = bin(x)[2:]
#         for xx in x:
#             if xx == "1":
#                 prefix += 1
#             else:
#                 break
#     return prefix
#
# print(maske(max(list_block), min(list_block)))
# print(get_prefix(maske(max(list_block), min(list_block))))
# print(sub_net(list_block, maske(max(list_block), min(list_block))))
# # 1011 1111
# # 1100 0010
#
#
