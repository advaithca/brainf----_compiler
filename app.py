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
A = st.button('Compile')
B = st.button("Run with an example")
with plh.container():
    if A:
        if code:
            with st.spinner('Compiling..'):
                st.success('Output : ')
                bf = BrainFuck(200)
                try:
                    x = bf.compile(code)
                except:
                    st.error("An Error has occured.")
                else:
                    st.success("Successfully compiled!!")
                    st.text(''.join(x))
        else:
            st.error("Enter something before compiling, pls.")

    if B:
        code = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
        st.write("Running with: ")
        st.code(code)
        with st.spinner('Compiling..'):
            x = []
            st.success('Compiled Successfully..')
            bf = BrainFuck(200)
            x = bf.compile(code)
            st.text(''.join(x))

if st.button('Clear'):
    plh.empty()