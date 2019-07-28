import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

class BodyText extends React.Component {
  render() {
    return (
      <View style={styles.memoList}>
        <View style={styles.memoListItem}>
          <Text style={styles.memoTitle}>めも</Text>
          <Text style={styles.memoDate}>2017/10/10</Text>
        </View>
        <View style={styles.memoListItem}>
          <Text style={styles.memoTitle}>めも</Text>
          <Text style={styles.memoDate}>2017/10/10</Text>
        </View>
        <View style={styles.memoListItem}>
          <Text style={styles.memoTitle}>めも</Text>
          <Text style={styles.memoDate}>2017/10/10</Text>
        </View>
        <View style={styles.memoListItem}>
          <Text style={styles.memoTitle}>めも</Text>
          <Text style={styles.memoDate}>2017/10/10</Text>
        </View>
        <View style={styles.memoListItem}>
          <Text style={styles.memoTitle}>めも</Text>
          <Text style={styles.memoDate}>2017/10/10</Text>
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  memoList: {
    width: '100%',
    // スクリーンいっぱいに広げる
    flex: 1,
  },
  memoListItem: {
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#ddd',
    backgroundColor: '#fff',
  },
  memoTitle: {
    fontSize: 18,
    marginBottom: 4,
  },
  memoDate: {
    fontSize: 12,
    color: '#a2a2a2',
  },
});

export default BodyText;
