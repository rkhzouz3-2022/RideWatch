import { StyleSheet, Text, View, TextInput, Switch, Pressable, Button } from "react-native";
import React, { useState, useEffect } from 'react'
import Styles from "./styles";

const CreateAccount = () => {

    const [serverData, setServerData] = useState([{}]);
    const [buttonSubmit, setButtonSubmit] = useState(false)

    // Need to change to not run on initial render (new hook?)
    useEffect(() => {
      fetch("http://127.0.0.1:5000/createAccount").then(
        res => res.json()
      ).then(
        data => {
          setServerData(data)
          console.log(data)
        }
      )
    }, [buttonSubmit])

    const [parentAccount, setParentAccount] = useState(false);

  return (
    <View>
        <TextInput style={Styles.loginBoxes} placeholder="Username" />
        <TextInput style={Styles.loginBoxes} placeholder="Password" secureTextEntry />
        <View>
            <Text>Parent Account?</Text>
            <Switch value={parentAccount} onValueChange={() => setParentAccount(!parentAccount)} />
        </View>

        <Button style={Styles.submitBox} title="Create Account" onPress={() => setButtonSubmit(true)}/>
    </View>
  )
}

export default CreateAccount