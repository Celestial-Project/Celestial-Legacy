const get_response = async (message: string = ""): Promise<string> => {

    const response = await fetch('http://127.0.0.1:5000/celestial-api', {
      method: 'POST',
      mode: 'cors',
      cache: 'no-cache', 
      credentials: 'same-origin', 
      headers: {
        'Content-Type': 'application/json',
        'Accept': '*/*'
      },
      redirect: 'follow', 
      referrerPolicy: 'no-referrer',
      body: JSON.stringify({
        message: message
      })
    })

    const data = await response.json()
    console.log(data)

    return data.chat

}

export default get_response