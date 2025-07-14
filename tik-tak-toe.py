import streamlit as st

# Initialize state
if "count_key" not in st.session_state:
    st.session_state.count_key = 0
if "flag" not in st.session_state:
    st.session_state.flag = True
if "numbers" not in st.session_state:
    st.session_state.numbers = [1,2,3,4,5,6,7,8,9]
if "board" not in st.session_state:
    st.session_state.board = ['   '] * 9  # Positions 0 to 8

# Draw board
def cross_board():
    b = st.session_state.board
    st.write(f'       |       |       ')
    st.write(f'  {b[0]}  |  {b[1]}  |  {b[2]}  ')
    st.write(f'       |       |       ')
    st.write(f'-----------------------')
    st.write(f'       |       |       ')
    st.write(f'  {b[3]}  |  {b[4]}  |  {b[5]}  ')
    st.write(f'       |       |       ')
    st.write(f'-----------------------')
    st.write(f'       |       |       ')
    st.write(f'  {b[6]}  |  {b[7]}  |  {b[8]}  ')
    st.write(f'       |       |       ')

# Check winner
def winner_check():
    b = st.session_state.board
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for w in wins:
        if b[w[0]] == b[w[1]] == b[w[2]] and b[w[0]] != '   ':
            st.write(f"🎉 Player {'1' if b[w[0]] == ' X ' else '2'} wins!")
            st.session_state.flag = False
            return True
    return False

# Player input
def user_input():
    key = st.session_state.count_key
    move = st.number_input("Select a position (1-9):", 1, 9, key=f"move_{key}")
    if st.button("Submit", key=f"submit_{key}"):
        if move in st.session_state.numbers:
            st.session_state.numbers.remove(move)
            symbol = ' X ' if key % 2 == 0 else ' O '
            st.session_state.board[move - 1] = symbol
            st.session_state.count_key += 1
            if not winner_check() and st.session_state.count_key == 9:
                st.write(" Game ends in a draw.")
                st.session_state.flag = False
            st.rerun()
        else:
            st.warning("Position already taken.")

# Show board
st.title("Tic Tac Toe - Streamlit Version")
cross_board()

# Play
if st.session_state.flag:
    user_input()
else:
    st.success(" Game Over!")

# Reset button
if st.button("Reset Game"):
    st.session_state.clear()
    st.rerun()
