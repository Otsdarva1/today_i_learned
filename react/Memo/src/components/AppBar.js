import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

class AppBar extends React.Component {
  render() {
    return (
      <View style={styles.appbar}>
        <View>
          <Text style={styles.appbarItem}>MEMOT</Text>
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  appbar:{
    // 位置固定
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    height: 90,
    // iphone10のためのパディング
    paddingTop: 30,
    backgroundColor: '#265366',
    // 内容が上下左右のセンターに
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width:0, height:0 },
    shadowOpacity: 0.3,
    shadowRadius: 3,
    zIndex: 10,
  },
  appbarItem:{
    color: '#fff',
    fontSize: 20,
  },
});

export default AppBar;
