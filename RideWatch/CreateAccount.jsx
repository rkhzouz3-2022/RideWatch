import { StyleSheet, Text, View, TextInput, Switch, Pressable, Button } from "react-native";
import React, {useState} from 'react'
import Styles from "./styles";

const CreateAccount = () => {

    const [parentAccount, setParentAccount] = useState(false);

  return (
    <View>
        <TextInput style={Styles.loginBoxes} placeholder="Username" />
        <TextInput style={Styles.loginBoxes} placeholder="Password" secureTextEntry />
        <View>
            <Text>Parent Account?</Text>
            <Switch value={parentAccount} onValueChange={() => setParentAccount(!parentAccount)} />
        </View>

        <Button style={Styles.submitBox} title="Create Account" />
    </View>
  )
}

export default CreateAccount