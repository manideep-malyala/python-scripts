def cacipher(message, key, mode):
    z_val = key%26 if mode == 'en' else 26 - key%26
    m_string = ''
    for evC in message:
      if evC.isalpha():
        mCode = (ord(evC) - 96) + z_val
        if mCode > 26:
          m_string+=chr(96 + mCode%26)
        else:
          m_string+=chr(96 + mCode)
      else:
        m_string+=evC
    print("Message Encoded To :" if mode=='en' else "Message Decoded To:","{}".format(m_string))
