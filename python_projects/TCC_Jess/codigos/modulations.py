import numpy as np


def bit_to_QPSK(TX_bit):
    temp = TX_bit.shape
    M = temp[0]
    bit_num = temp[1]

    TX_BPSK = np.ones((M, bit_num))
    TX_BPSK[TX_bit == 0] = -1

    TX_BPSK = TX_BPSK * 1 / np.sqrt(2)
    TX_QPSK1 = TX_BPSK[:, 0:bit_num:2]
    TX_QPSK2 = + 1j*TX_BPSK[:, 1:bit_num:2]
    return TX_QPSK1 + TX_QPSK2


def bit_to_16QAM(TX_bit):

    temp = TX_bit.shape
    M = temp[0]
    bit_num = temp[1]
    sym_num = bit_num / 4

    TX_BPSK = np.ones((M, bit_num))
    TX_BPSK[TX_bit == 0] = -1

    temp = 2 * TX_BPSK[:, 0:bit_num:2] + TX_BPSK[:, 1:bit_num:2]

    temp_copy = temp.copy()
    temp[temp_copy == 3] = 1
    temp[temp_copy == 1] = 3

    TX_16QAM = (temp[:, 0:int(sym_num * 2):2] + 1j * temp[:, 1:int(sym_num * 2):2]) * 1 / np.sqrt(10)

    return TX_16QAM


def bit_to_64QAM(TX_bit):
    temp = TX_bit.shape
    M = temp[0]
    bit_num = temp[1]
    sym_num = bit_num / 4

    TX_BPSK = np.ones((M, bit_num))
    TX_BPSK[TX_bit == 0] = -1

    temp = 4 * TX_BPSK[:, 0:bit_num:3] + 2 * TX_BPSK[:, 1:bit_num:3] + TX_BPSK[:, 2:bit_num:3]

    temp_copy = temp.copy()
    temp[temp_copy == 7] = 3
    temp[temp_copy == 5] = 1
    temp[temp_copy == 3] = 5
    temp[temp_copy == 1] = 7
    temp[temp_copy == -3] = -1
    temp[temp_copy == -1] = -3

    TX_64QAM = (temp[:, 0:int(sym_num * 3):2] + 1j * temp[:, 1:int(sym_num * 3):2]) * 1 / np.sqrt(42)

    return TX_64QAM

def QPSK_to_bit(RX_symbol):
    temp = RX_symbol.shape
    N = temp[0]
    sym_num = temp[1]
    bit_num = sym_num * 2

    odd_bit = np.real(RX_symbol)
    odd_bit[odd_bit > 0] = 1
    odd_bit[odd_bit < 0] = 0

    even_bit = np.imag(RX_symbol)
    even_bit[even_bit > 0] = 1
    even_bit[even_bit < 0] = 0

    RX_bit = np.zeros((N, bit_num))
    RX_bit[:, 0:bit_num:2] = odd_bit
    RX_bit[:, 1:bit_num:2] = even_bit

    return RX_bit


def QAM16_to_bit(RX_symbol):
    temp = RX_symbol.shape
    N = temp[0]
    sym_num = temp[1]
    bit_num = sym_num * 4

    RX_symbol = RX_symbol * np.sqrt(10)

    RX_symbol_real = np.real(RX_symbol)
    RX_symbol_imag = np.imag(RX_symbol)

    real_copy = RX_symbol_real.copy()
    imag_copy = RX_symbol_imag.copy()

    RX_symbol_real[real_copy > 2] = 3
    RX_symbol_real[2 > real_copy] = 1
    RX_symbol_real[0 > real_copy] = -1
    RX_symbol_real[-2 > real_copy] = -3

    RX_symbol_imag[imag_copy > 2] = 3
    RX_symbol_imag[2 > imag_copy] = 1
    RX_symbol_imag[0 > imag_copy] = -1
    RX_symbol_imag[-2 > imag_copy] = -3

    temp = np.zeros((N, sym_num * 2))
    temp[:, 0:sym_num*2:2] = RX_symbol_real
    temp[:, 1:sym_num*2:2] = RX_symbol_imag

    temp2 = np.zeros((N, sym_num * 2)) + 1j * np.zeros((N, sym_num * 2))
    temp2[temp == 3] = 1 - 0j
    temp2[temp == 1] = 1 + 1j
    temp2[temp == -1] = - 0 + 1j
    temp2[temp == -3] = - 0 - 0j

    RX_bit = np.zeros((N, bit_num))
    RX_bit[:, 0:bit_num:2] = np.real(temp2)
    RX_bit[:, 1:bit_num:2] = np.imag(temp2)

    return RX_bit

def QAM64_to_bit(RX_symbol):
    temp = RX_symbol.shape
    N = temp[0]
    sym_num = temp[1]
    bit_num = sym_num * 6

    RX_symbol = RX_symbol * np.sqrt(42)

    RX_symbol_real = np.real(RX_symbol)
    RX_symbol_imag = np.imag(RX_symbol)

    real_copy = RX_symbol_real.copy()
    imag_copy = RX_symbol_imag.copy()

    RX_symbol_real[real_copy > 6] = 7
    RX_symbol_real[6 > real_copy] = 5
    RX_symbol_real[4 > real_copy] = 3
    RX_symbol_real[2 > real_copy] = 1
    RX_symbol_real[0 > real_copy] = -1
    RX_symbol_real[-2 > real_copy] = -3
    RX_symbol_real[-4 > real_copy] = -5
    RX_symbol_real[-6 > real_copy] = -7

    RX_symbol_imag[imag_copy > 6] = 7
    RX_symbol_imag[6 > imag_copy] = 5
    RX_symbol_imag[4 > imag_copy] = 3
    RX_symbol_imag[2 > imag_copy] = 1
    RX_symbol_imag[0 > imag_copy] = -1
    RX_symbol_imag[-2 > imag_copy] = -3
    RX_symbol_imag[-4 > imag_copy] = -5
    RX_symbol_imag[-6 > imag_copy] = -7

    temp = np.zeros((N, sym_num * 2))
    temp[:, 0:sym_num*2:2] = RX_symbol_real
    temp[:, 1:sym_num*2:2] = RX_symbol_imag

    RX_bit_first = np.zeros((N, int(bit_num/3)))
    RX_bit_first[temp > 0] = 1
    RX_bit_first[temp < 0] = 0

    RX_bit_second = np.zeros((N, int(bit_num / 3)))
    RX_bit_second[temp == 7] = 0
    RX_bit_second[temp == 5] = 0
    RX_bit_second[temp == 3] = 1
    RX_bit_second[temp == 1] = 1
    RX_bit_second[temp == -1] = 1
    RX_bit_second[temp == -3] = 1
    RX_bit_second[temp == -5] = 0
    RX_bit_second[temp == -7] = 0

    RX_bit_third = np.zeros((N, int(bit_num / 3)))
    RX_bit_third[temp == 7] = 0
    RX_bit_third[temp == 5] = 1
    RX_bit_third[temp == 3] = 1
    RX_bit_third[temp == 1] = 0
    RX_bit_third[temp == -1] = 0
    RX_bit_third[temp == -3] = 1
    RX_bit_third[temp == -5] = 1
    RX_bit_third[temp == -7] = 0

    RX_bit = np.zeros((N, bit_num))
    RX_bit[:, 0:bit_num:3] = RX_bit_first
    RX_bit[:, 1:bit_num:3] = RX_bit_second
    RX_bit[:, 2:bit_num:3] = RX_bit_third

    return RX_bit
if __name__ == '__main__':
    import projeto_tcc_jessica
    M = 1
    N = M

    bit_num = 12

    TX_bit = np.random.randint(0, 2, (1, bit_num))
    print(TX_bit)
    TX_QPSK= bit_to_QPSK(TX_bit)
    TX_copy= np.copy(TX_QPSK)
    print(TX_copy)
