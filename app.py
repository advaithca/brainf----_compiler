import streamlit as st

from bf import BrainFuck

st.write('''
# Just another BrainF--ck compiler:joy:
****
''')
with st.sidebar:
    st.write('''### *BrainF--ck*''')
    st.image('bf.png')
    st.write('''****''')
    st.write('''*[BrainF--ck](https://en.wikipedia.org/wiki/Brainfuck) is one of the most famous esoteric programming languages 
                and it was created by Urban Müller.*''')
    with st.expander("Syntax"):
        st.write('''
        | Syntax | Description |
        | ----------- | ----------- |
        | > | Move memory pointer to the right once |
        | < | Move memory pointer to the left once |
        | + | Increment value at pointer by 1 |
        | - | Decrement value at pointer by 1 |
        | [ | Skip to corresponding ']' if value at pointer is 0 |
        | ] | Skip to corresponding '[' if value at pointer isn't 0 |

        Everything else is considered as a comment.
        ''')
st.write('''You can input your BrainF--ck code in the text box and get the output, It's as simple as that.

User input for the program isn't supported yet :disappointed:
''')

code = st.text_area(label='Input code',height=300)
plh = st.empty()

if st.button('Compile'):
    if code:
        plh.empty()
        with st.spinner('Compiling..'):
            x = []
            st.success('Output : ')
            bf = BrainFuck(200)
            x = bf.compile(code)
            with plh.container():
                st.text(''.join(x))
    else:
        st.error("Enter something before compiling, pls.")

if st.button("Run with an example"):
    plh.empty()
    code = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
    st.write("Running with: ")
    st.code(code)
    with st.spinner('Compiling..'):
        x = []
        st.success('Output : ')
        bf = BrainFuck(200)
        x = bf.compile(code)
        with plh.container():
            st.text(''.join(x))