import {createClient} from '@supabase/supabase-js'

const supabaseUrl = 'https://grpyzglacfygoswckzoq.supabase.co'
const supabaseKey = 'sb_publishable_kwftQSUL4wzptu-c5gN3lg_cHRb8i2a'

export const supabase = createClient(supabaseUrl, supabaseKey)